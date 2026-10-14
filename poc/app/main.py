from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

app = FastAPI()

# In-memory storage: cleared whenever the backend restarts.
posts = []  # each item: {"post_id": int, "body": str}


class PostIn(BaseModel):
    body: str  # Pydantic v2 rejects numbers, booleans and null here instead of converting them


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request, exc):
    # FastAPI rejected the request before our route ran.
    # Turn its error list into the single message the contract requires.
    error = exc.errors()[0]
    if error["type"] == "json_invalid":
        message = "Request body must be valid JSON."
    elif error["loc"] == ("body",):  # the whole body is wrong: array, string, number, null
        message = "Request body must be a JSON object."
    elif error["type"] == "missing":  # loc is ("body", "body"): our field is absent
        message = "The body field is required."
    else:
        message = "Post body must be a string."
    return JSONResponse(status_code=422, content={"detail": message})


@app.get("/")
async def index():
    return FileResponse(Path(__file__).parent / "index.html")


@app.post("/posts", status_code=201)
async def create_post(post: PostIn):
    text = post.body.strip()
    # len() counts Unicode code points, as the contract specifies.
    if not 1 <= len(text) <= 2000:
        raise HTTPException(status_code=422, detail="Post body must contain 1–2000 characters after trimming.")
    # Posts are never deleted, so the next ID is the list length plus one.
    # No await between here and append, so two requests cannot get the same ID.
    new_post = {"post_id": len(posts) + 1, "body": text}
    posts.append(new_post)
    return new_post


@app.get("/posts")
async def list_posts():
    # Posts are appended in ID order, so reversing gives newest first.
    return list(reversed(posts))

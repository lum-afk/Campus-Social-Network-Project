import pytest
from fastapi.testclient import TestClient

from app.main import app, posts

client = TestClient(app)

LENGTH_ERROR = {"detail": "Post body must contain 1–2000 characters after trimming."}


@pytest.fixture(autouse=True)
def empty_store():
    # Every test starts with no posts, like a freshly started backend.
    posts.clear()


def post_raw(raw):
    # Send exact bytes, so we can test malformed and non-object JSON.
    return client.post("/posts", content=raw, headers={"Content-Type": "application/json"})


def test_empty_feed():
    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json() == []


def test_create_trims_surrounding_whitespace():
    response = client.post("/posts", json={"body": "  Our fictional coding club meets on Thursday.  "})
    assert response.status_code == 201
    assert response.json() == {"post_id": 1, "body": "Our fictional coding club meets on Thursday."}


def test_internal_spaces_and_line_breaks_are_kept():
    response = client.post("/posts", json={"body": " a  b\nc "})
    assert response.json()["body"] == "a  b\nc"


def test_ids_increase_and_feed_is_newest_first():
    client.post("/posts", json={"body": "Our first announcement."})
    client.post("/posts", json={"body": "Welcome to the club!"})
    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json() == [
        {"post_id": 2, "body": "Welcome to the club!"},
        {"post_id": 1, "body": "Our first announcement."},
    ]


def test_malformed_json():
    response = post_raw('{"body": ')
    assert response.status_code == 422
    assert response.json() == {"detail": "Request body must be valid JSON."}


@pytest.mark.parametrize("raw", ["[]", '"text"', "5", "null"])
def test_json_that_is_not_an_object(raw):
    response = post_raw(raw)
    assert response.status_code == 422
    assert response.json() == {"detail": "Request body must be a JSON object."}


def test_empty_request_body_is_treated_as_not_an_object():
    # Not listed in the contract; this records the behaviour we chose to accept.
    response = post_raw("")
    assert response.status_code == 422
    assert response.json() == {"detail": "Request body must be a JSON object."}


@pytest.mark.parametrize("raw", ["{}", '{"other": "x"}'])
def test_missing_body_field(raw):
    response = post_raw(raw)
    assert response.status_code == 422
    assert response.json() == {"detail": "The body field is required."}


@pytest.mark.parametrize("value", [5, 1.5, True, None, ["a"], {"a": 1}])
def test_non_string_body_is_rejected_without_conversion(value):
    response = client.post("/posts", json={"body": value})
    assert response.status_code == 422
    assert response.json() == {"detail": "Post body must be a string."}


@pytest.mark.parametrize("body", ["", "   ", " \n\t "])
def test_empty_or_whitespace_only_body(body):
    response = client.post("/posts", json={"body": body})
    assert response.status_code == 422
    assert response.json() == LENGTH_ERROR


def test_2000_characters_accepted():
    response = client.post("/posts", json={"body": "a" * 2000})
    assert response.status_code == 201


def test_2001_characters_rejected():
    response = client.post("/posts", json={"body": "a" * 2001})
    assert response.status_code == 422
    assert response.json() == LENGTH_ERROR


def test_emoji_count_as_one_code_point_each():
    # Each emoji is 1 code point but 2 UTF-16 units; the contract counts code points.
    assert client.post("/posts", json={"body": "😀" * 2000}).status_code == 201
    response = client.post("/posts", json={"body": "😀" * 2001})
    assert response.status_code == 422
    assert response.json() == LENGTH_ERROR


def test_limit_is_checked_after_trimming():
    response = client.post("/posts", json={"body": "  " + "a" * 2000 + "\n"})
    assert response.status_code == 201
    assert response.json()["body"] == "a" * 2000


def test_rejected_requests_do_not_use_an_id():
    post_raw("{}")
    client.post("/posts", json={"body": "   "})
    response = client.post("/posts", json={"body": "First real post"})
    assert response.json() == {"post_id": 1, "body": "First real post"}
    assert client.get("/posts").json() == [{"post_id": 1, "body": "First real post"}]


def test_html_is_stored_unchanged():
    response = client.post("/posts", json={"body": "<b>hi</b>"})
    assert response.json()["body"] == "<b>hi</b>"


def test_page_is_served():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "Publish" in response.text

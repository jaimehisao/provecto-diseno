from fastapi.testclient import TestClient
from backend.application import app
from unittest import mock

from backend.dto.post import Post
from backend.dto.comment import Comment

client = TestClient(app)

"""
@mock.patch("pymongo.collection.Collection.find")
def test_name(self, mock_find):
    mock_find.return_value = {'name' : 'Kelly', 'email' : 'kelly@gmail.com'}
    # rest of test
"""

@mock.patch("backend.database.post_db.find_one")
def test_like_post(find_one_mock):
    find_one_mock.return_value = Post(id="1", body="body", image_path="path", user_id="1", created_at="2021-01-01", likes=0, comments=[])
    with mock.patch("backend.operations.like_post") as mock_like_post:
        mock_like_post.return_value = True
        response = client.post("/post/like/1")
        assert response.status_code == 200
        assert response.json() == "Post liked"


"""

def test_database_get_user_posts():
    with mock.patch("backend.database.get_user_posts") as mock_get_user_posts:
        mock_get_user_posts.return_value = [
            Post(
                _id=1,
                body="My first post!",
                image_path="images/1.jpg",
                user_id="jaimehisao",
                created_at="2020-01-01",
                comments=[
                    Comment(
                        body="This is a comment",
                        user_id="jaimehisao",
                        post_id=1,
                        created_at="2020-01-01",
                        likes=2
                    )
                ]
            )
        ]
        response = client.get("/posts/user/1")
        assert response.status_code == 200
        assert (
            response.json() == "_id: 1, body:My first post!, "
            "image_path:images/1.jpg, "
            "user_id:jaimehisao, "
            "created_at:2020-01-01, "
            "comments:[{body:This is a comment, "
            "user_id:jaimehisao, "
            "post_id:1, "
            "reated_at:2020-01-01, "
            "likes:2,}]"
        )

"""
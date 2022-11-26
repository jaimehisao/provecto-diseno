from dto.post import Post
from dto.comment import Comment

from operations import create_new_post

posts = [
    Post(
        id=1,
        body="My first post!",
        image_path="1.jpg",
        user_id="jaimehisao",
        created_at="2020-01-01",
        likes=0,
        comments=[
            Comment(
                body="This is a comment",
                user_id="jaimehisao",
                post_id=1,
                created_at="2020-01-01",
                likes=2
            )
        ]
    ),
    Post(
        id=2,
        body="My first post!",
        image_path="2.jpg",
        user_id="mariomoo",
        created_at="2020-01-01",
        likes=0,
        comments=[
            Comment(
                body="Welcome to Exchangeagram!",
                user_id="jaimehisao",
                post_id=2,
                created_at="2020-01-01",
                likes=0
            )
        ]
    ),
    Post(
        id=3,
        body="My first post!",
        image_path="3.jpg",
        user_id="jpdixon",
        created_at="2020-01-01",
        likes=0,
        comments=[
            Comment(
                body="Welcome to Exchangeagram!",
                user_id="mariomoo",
                post_id=3,
                created_at="2020-01-01",
                likes=3
            )
        ]
    )
]

for post in posts:
    create_new_post(post)

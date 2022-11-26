import logging
import datetime
import uuid

from fastapi import FastAPI, Body, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from operations import (
    save_image,
    post_upsert,
    get_post_by_id,
    like_post,
    create_new_comment_in_post,
    unlike_post,
    get_all_posts,
)
from dto.comment_body import CommentBody
from dto.comment import Comment
from dto.post import Post, PostUpload

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


############### Post Routes ###############
# LGTM
@app.get("/post/image/{image_path}")
def get_image_path(image_path: str):
    """
    Returns and image that matches the path in the backend.
    :param image_path: Image path that is needed
    :return: Imagestream
    """
    logging.info("Getting image path: " + image_path)
    return FileResponse("images/" + image_path)


@app.get("/posts")
def get_all_posts_endpoint():
    """
    Returns all the posts in the database.
    :return: List of posts.
    """
    logging.info("Getting all posts")
    posts = get_all_posts()
    return JSONResponse(content=jsonable_encoder(posts))


# LGTM
@app.get("/post/id/{post_id}")
def get_post_by_id_endpoint(post_id: str):
    """
    Gets an individual post by its ID
    :param post_id: post id needed
    :return: returns the post
    """
    post = get_post_by_id(post_id)
    if post is None:
        return JSONResponse(status_code=404, content="Post not found")
    return JSONResponse(content=jsonable_encoder(post))


# LGTM
@app.post("/post/like/{post_id}")
def like_post_endpoint(post_id: str):
    success = like_post(post_id)
    if success:
        return JSONResponse(status_code=200, content="Post liked")
    return JSONResponse(status_code=404, content="Post not found")


# LGTM
@app.post("/post/unlike/{post_id}")
def dislike_post_endpoint(post_id: str):
    success = unlike_post(post_id)
    if success:
        return JSONResponse(status_code=200, content="Post unliked")
    return JSONResponse(status_code=404, content="Post not found")


"""
@app.delete("/post/delete")
def delete_post_endpoint(post_id: str):
    success = delete_post(post_id)
    if success:
        return JSONResponse(status_code=200, content="Post deleted")
    return JSONResponse(status_code=404, content="Post not found")
    

@app.post("/post/new")
def create_new_post_endpoint(post: Post):
    success = create_new_post(post)
    if success:
        return JSONResponse(status_code=201, content="Post created")
    return JSONResponse(status_code=500, content="Post not created")
    
@app.get("/posts/user/{user_id}")
def get_all_posts_from_user(user_id: str):
    Retrieve all posts from a user
    :param user_id: user ID from which posts will be retrieved
    :return: returns an object with the user's posts (except images)
    logging.info("Getting all posts from user with id: " + user_id)
    posts = get_user_posts(user_id)
    return_posters = []
    if posts is None:
        return JSONResponse(status_code=404, content="User has no posts.")
    for post in posts:
        tmp = Post()
        tmp.id = post["id"]
        tmp.body = post["body"]
        tmp.image_path = post["image"]
        tmp.user_id = post["user_id"]
        tmp.created_at = post["created_at"]
        return_posters.append(tmp)
    return JSONResponse(content=jsonable_encoder(return_posters))
"""


############### Comment Routes ###############
@app.post("/post/comments/add")
def create_new_comment_in_post_endpoint(item: CommentBody):
    """
    Adds new comment to an existing post
    :param post_id: Post ID to add the comment to
    :param user_id: User ID of the comment poster
    :param comment_body: Text of the comment
    :return: T/F depending on success
    """
    print("Adding comment to post: " + item.post_id)
    print("Comment body: " + item.comment_body)
    print("User ID: " + item.user_id)
    success = create_new_comment_in_post(
        item.post_id,
        Comment(
            body=item.comment_body,
            user_id=item.user_id,
            post_id=item.post_id,
            created_at=str(datetime.date.today()),
            likes=0,
        ),
    )
    if success:
        return JSONResponse(status_code=200, content="Comment added")
    return JSONResponse(status_code=404, content="Adding comment failed")


image_name = None


@app.post("/post/new")
def create_new_post_endpoint(post_upload: PostUpload):
    _id = str(uuid.uuid4())
    # print("Creating new post with id: " + str(dict(post_upload)))
    post = Post(
        id=_id,
        body=post_upload.body,
        image_path=post_upload.image_name,
        user_id=post_upload.user_id,
        created_at=str(datetime.date.today()),
        likes=0,
        comments=[]
    )
    # print("Post: " + str(dict(post)))
    success = post_upsert(post)
    global image_name
    image_name = post_upload.image_name
    if success:
        return JSONResponse(status_code=200, content="Post created")
    return JSONResponse(status_code=500, content="Post not created")


@app.post("/post/new/image")
async def add_image_to_new_post(file: UploadFile = File(...)):
    """
    contents = file.file.read()
    global image_name
    save_image(image_name, contents)
    return JSONResponse(status_code=200, content="Image Added")
    """
    return {"filename": file.filename}

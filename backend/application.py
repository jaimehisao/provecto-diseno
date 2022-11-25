import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse


from database import get_user_posts, get_user, get_post_by_id, \
    like_post, create_new_comment, unlike_post
from dto.post import Post
from dto.comment import Comment

app = FastAPI()


############### Post Routes ###############
@app.get("/posts/user/{user_id}")
def get_all_posts_from_user(user_id: str):
    """
    Retrieve all posts from a user
    :param user_id: user ID from which posts will be retrieved
    :return: returns an object with the user's posts (except images)
    """
    logging.info("Getting all posts from user with id: " + user_id)
    posts = get_user_posts(user_id)
    return_posters = []
    if posts is None:
        return JSONResponse(status_code=404, content="User has no posts.")
    for post in posts:
        tmp = Post()
        tmp.id = post['id']
        tmp.body = post['body']
        tmp.image_path = post['image']
        tmp.user_id = post['user_id']
        tmp.created_at = post['created_at']
        return_posters.append(tmp)
    return JSONResponse(content=jsonable_encoder(return_posters))


@app.get("/post/image/{image_path}")
def get_image_path(image_path: str):
    """
    Returns and image that matches the path in the backend.
    :param image_path: Image path that is needed
    :return: Imagestream
    """
    logging.info("Getting image path: " + image_path)
    return FileResponse(image_path)


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
    tmp = Post()
    tmp.id = post['id']
    tmp.body = post['body']
    tmp.image_path = post['image']
    tmp.user_id = post['user_id']
    tmp.created_at = post['created_at']
    return JSONResponse(content=jsonable_encoder(tmp))


@app.post("/post/like")
def like_post_endpoint(post_id: int):
    success = like_post(post_id)
    if success:
        return JSONResponse(status_code=200, content="Post liked")
    return JSONResponse(status_code=404, content="Post not found")


@app.post("/post/unlike")
def dislike_post_endpoint(post_id: int):
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
"""



############### Comment Routes ###############
@app.post("/comments/post/add")
def create_new_comment_in_post(post_id: int, comment_body: str):
    success = create_new_comment(post_id, comment_body)  # need to add user that put comment too...
    if success:
        return JSONResponse(status_code=200, content="Comment added")
    return JSONResponse(status_code=404, content="Adding comment failed")


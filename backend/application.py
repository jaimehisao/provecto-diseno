from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


from database import get_user_posts, get_user, get_post_by_id, \
    like_post, create_new_comment, unlike_post, delete_post, create_new_post
from dto.post import Post
from dto.comment import Comment

app = FastAPI()


############### Post Routes ###############
@app.get("/posts/user")
def get_all_posts_from_user(user_id: str):
    posts = get_user_posts(user_id)
    return_posters = []
    if posts is None:
        return JSONResponse(status_code=404, content="User not found")
    for post in posts:
        tmp = Post()
        tmp.id = post['id']
        tmp.location = post['location']
        tmp.body = post['body']
        tmp.image = post['image']
        tmp.user_id = post['user_id']
        tmp.created_at = post['created_at']
        return_posters.append(tmp)
        #  case if there are no posts?
    return JSONResponse(content=jsonable_encoder(return_posters))


@app.get("/post/id")
def get_post_by_id(post_id: int):
    return JSONResponse(content=jsonable_encoder(get_post_by_id(post_id)))


@app.post("/post/new")
def create_new_post_endpoint(post: Post):
    create_new_post(post)
    return JSONResponse(status_code=200, content="Post created")


@app.post("/post/like")
def like_post_endpoint(post_id: int):
    like_post(post_id)
    return JSONResponse(status_code=200, content="Post liked")


@app.post("/post/unlike")
def dislike_post_endpoint(post_id: int):
    unlike_post(post_id)
    return JSONResponse(status_code=200, content="Post unliked")


@app.delete("/post/delete")
def delete_post_endpoint(post_id: str):
    delete_post(post_id)
    return JSONResponse(status_code=200, content="Post deleted")


############### Comment Routes ###############
@app.post("/comments/post/add")
def create_new_comment_in_post(post_id: int, comment_body: str):
    create_new_comment(post_id, comment_body)  # need to add user that put comment too...
    return JSONResponse(status_code=200, content="Comment added")


@app.delete("/comments/post/delete")
def delete_comment_in_post(post_id: int, comment_id: int):
    #  delete comment in post
    return JSONResponse(status_code=200, content="Comment deleted")


############### User Management Routes ###############
@app.post("/logout")
def login(user):  # User object pending
    pass


@app.post("/login")
def logout(user):  # User object pending
    pass

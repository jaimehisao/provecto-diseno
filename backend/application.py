from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


from database import get_user_posts, get_user, get_post_by_id, like_post, create_new_comment, unlike_post
from dto.post import Post
from dto.comment import Comment

app = FastAPI()


############### Post Routes ###############
@app.get("/posts/user")
def get_all_posts_from_user(user_id: str):
    posts = get_user_posts(user_id)
    return_posters = []
    for post in posts:
        tmp = Post()
        tmp.id = post['id']
        tmp.location = post['location']
        tmp.body = post['body']
        tmp.image = post['image']
        tmp.user_id = post['user_id']
        tmp.created_at = post['created_at']
        return_posters.append(tmp)
    return JSONResponse(content=jsonable_encoder(return_posters))


@app.get("/post/id")
def get_post_by_id(post_id: int):
    return JSONResponse(content=jsonable_encoder(get_post_by_id(post_id)))


@app.post("/post/new")
def create_new_post(post_id: int):
    pass


@app.post("/post/like")
def like_post(post_id: int):
    like_post(post_id)
    return 200


@app.post("/post/unlike")
def dislike_post_endpoint(post_id: int):
    unlike_post(post_id)


@app.delete("/post/delete")
def delete_post(post_id: int):
    pass


############### Comment Routes ###############
@app.post("/comments/post/add")
def create_new_comment_in_post(post_id: int, comment_body: str):
    create_new_comment(post_id, comment_body)  # need to add user that put comment too...


@app.delete("/comments/post/delete")
def delete_comment_in_post(post_id: int, comment_id: int):
    return None

############### User Management Routes ###############
@app.post("/logout")
def login(user):  # User object pending
    pass


@app.post("/login")
def logout(user):  # User object pending
    pass

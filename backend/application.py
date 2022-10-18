from fastapi import FastAPI

app = FastAPI()


############### Post Routes ###############
@app.get("/posts/user")
def get_all_posts_from_user(user_id: int):
    pass


@app.get("/post/id")
def get_post_by_id(post_id: int):
    pass


@app.post("/post/new")
def create_new_post(post_id: int):
    pass


@app.post("/post/like")
def like_post(post_id: int):
    pass


@app.post("/post/unlike")
def unlike_post(post_id: int):
    pass


@app.delete("/post/delete")
def delete_post(post_id: int):
    pass


############### Comment Routes ###############
@app.get("/comments/post")
def create_new_comment_in_post(post_id: int, comment_body: str):
    pass


@app.delete("/comments/post")
def delete_comment_in_post(post_id: int, comment_id: int):
    return None


@app.post("/comments/like")
def like_comment_in_post(post_id: int, comment_id: int):
    return None


@app.delete("/comments")
def delete_comment_in_post(post_id: int, comment_id: int):
    return None


############### User Management Routes ###############

@app.post("/user/new")
def create_new_user(user):  # User object pending
    pass


@app.post("/user/change_password")
def change_user_password(user):  # User object pending
    pass


@app.post("/logout")
def login(user):  # User object pending
    pass


@app.post("/login")
def logout(user):  # User object pending
    pass

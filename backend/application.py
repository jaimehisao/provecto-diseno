from typing import Union

from fastapi import FastAPI

app = FastAPI()


### Post Routes ###
@app.get("/posts/user")
def get_all_posts_from_user(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/post/id")
def get_post_by_id(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/post/new")
def get_post_by_id(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


### Comment Routes ###
@app.get("/comments/post")
def create_new_comment_in_post():
    return None


@app.delete("/comments/post")
def delete_comment_in_post():
    return None


@app.put("/comments/like")
def like_comment_in_post():
    return None

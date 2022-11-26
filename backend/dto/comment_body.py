from pydantic import BaseModel


class CommentBody(BaseModel):
    comment_body: str
    user_id: str
    post_id: str

from pydantic import BaseModel


class Comment(BaseModel):
    body: str
    user_id: int
    post_id: int
    created_at: str
    likes: int  # Not sure if we should have this ability


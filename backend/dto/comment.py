from pydantic import BaseModel


class Comment(BaseModel):
    body: str
    user_id: str
    post_id: str
    created_at: str
    likes: int  # Not sure if we should have this ability


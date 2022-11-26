from pydantic import BaseModel
from .comment import Comment
from typing import List


class Post(BaseModel):
    id: str
    body: str
    image_path: str  # Path
    user_id: str
    created_at: str
    likes: int
    comments: List = []

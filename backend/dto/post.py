from pydantic import BaseModel
from .comment import Comment
from typing import List


class Post(BaseModel):
    id: int
    body: str
    image_path: str  # Path
    user_id: int
    created_at: str
    comments: List = []

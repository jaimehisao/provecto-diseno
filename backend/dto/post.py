from pydantic import BaseModel


class Post(BaseModel):
    id: int
    location: str
    body: str
    image: str  # Link to where we store it? Or what would be the correct way of storing it in the db?
    user_id: int
    created_at: str

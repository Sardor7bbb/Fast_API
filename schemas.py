from pydantic import BaseModel
from typing import Optional


class CreateBlog(BaseModel):
    username: str
    title: Optional[str]
    text: Optional[str]

    class Config:
        from_attributes = True


class DeleteBlog(BaseModel):
    username: str


class UpdateBlog(BaseModel):
    username: str
    title: Optional[str]
    text: Optional[str]
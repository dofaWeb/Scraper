"""create model by using pydantic for validating the value"""
from pydantic import BaseModel


class Blog(BaseModel):
    """a class for storing blog data"""
    date: str
    title: str
    author: str
    content: str
    comment: str
    label: list
from ninja import Schema, ModelSchema
from django.contrib.auth.models import User

from server.models import Images, Post


class Error(Schema):
    message: str

    
class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ["username", "email"]

class ImageSchema(ModelSchema):
    class Config:
        model = Images
        model_fields = ["alt_text", "description"]


class CategorySchema(Schema):
    name: str

class PostSchema(Schema):
    class Config:
        model = Post
        model_field = ["title", "content", "status", "category"]


class NewPost(Schema):
    class Config:
        model = Post
        model_field = ["title", "author", "content", "status", "category"]
    # title: str
    # content: str
    # status: str = None
    # category: CategorySchema

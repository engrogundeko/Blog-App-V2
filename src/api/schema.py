from ninja import Schema, ModelSchema

from src.server.models import Category, Images

class ImageSchema(ModelSchema):
    class Config:
        model = Images
        model_fields = [
            "id",
            "alt_text",
            "description",
            "link",
    ]
        

class CategoryShema(ModelSchema):
    class Config:
        model = Category
        model_fields = "name"

class PostSchema(Schema):
    id: int
    title: str
    author: str
    content: str
    status: str = None
    image: ImageSchema = None
    catogory = CategoryShema
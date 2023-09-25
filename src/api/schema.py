from datetime import date

from ninja import Schema, ModelSchema

from server.models import Category, Images

# class ImageSchema(ModelSchema):
#     class Config:
#         model = Images
#         model_fields = [
#             "id",
#             "alt_text",
#             "description",
#             "link",
#     ]
        

class CategoryShema(Schema):
    name: str

class PostSchema(Schema):
    title: str
    author: str
    content: str
    date_uploaded: date = None
    status: str = None
    image: str = None
    # image: ImageSchema = None
    catogory = CategoryShema


from ninja import NinjaAPI, File
from ninja.files import UploadedFile

from server.models import Post 
from .schema import PostSchema, ImageSchema, CategoryShema


api = NinjaAPI()


@api.get("/post")
def get_all_post(request, payload: PostSchema):
    qs = Post.objects.all()
    return qs

@api.post("/post", response={201: PostSchema})
def add_post(request, payload: PostSchema):
    payload_dict = payload.dict()
    post = Post(payload_dict)
    if not post.save():
        return 401, {"message": "Failed to save"}

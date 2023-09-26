from ninja import NinjaAPI, Router, Form, File
from ninja.files import UploadedFile
from typing import List
import os

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from server.models import Post, Category, Images
from .schema import ( Error, 
                    CategorySchema,
                    UserSchema,
                    PostSchema,
                    NewPost,
                    ImageSchema)

api = NinjaAPI()

""" To get all category or get category by id """
@api.get("/category", response = List[CategorySchema])
def get_all_category(request):
    qs = Category.objects.all()
    return qs

@api.get("/category/{category_name}", response= List[PostSchema])
def get_post_by_category(request, category_name: str)-> str:
    qs = Post.objects.filter(category__name=category_name)
    print(qs)
    return qs

# """ To delete category """
# @api.delete("/category/delete/{category_id}")
# def delete_category(request, category_id: int):
#     qs = get_object_or_404(Category, id=category_id)
#     return 200, {"message": "category has been deleted"}


""" To add new users """
@api.post("/accounts/new")
def create_account(request, username: str = Form(...),
                   password: str = Form(...)):
    try:
        hash_password = make_password(password)
        # print(hash_password)
        qs = User.objects.create_user(username=username, password=hash_password)
        return {"message": f"user with {qs.id} has been created successfully"}
    except Exception as e:
        return {"message": str(e)}


""" To create new post """
@api.post("/post", response=Error)
def create_post(request, 
                title: str = Form(...),
                content: str = Form(...),
                status:str = Form(...), 
                author:int = Form(...),
                category:str = Form(...),
                ):
    try: 
        authors = User.objects.get(pk=author)
        print(authors)
        qs = Post.objects.create(
            title = title,
            author = authors,
            content = content,
            status=status,
        )
        qs.category.set(category)
        qs.save()
        return {"message": "post has been created"}
    except (Exception, User.DoesNotExist) as e:
        return {"message": str(e)}


""" To get all post """
@api.get("/post", response = List[PostSchema])
def get_all_post(request):
    qs = Post.objects.all()
    # print(qs)
    return qs

""" To update post """
@api.put("/post{post_id}")
def update_post(request, post_id: int, payload: PostSchema = Form(...)):
    qs = get_object_or_404(Post, id=post_id)
    for attr, value in payload.dict().items():
        setattr(qs, attr, value)
    qs.save()
    return {"message": "Success"}

""" To delete post """
@api.delete("/post/{post_id}")
def delete_post(request, post_id: int)-> None:
    try:
        qs = get_object_or_404(Post, id=post_id)
        qs.delete()
        return 200, {"message": "delete was successful"}
    except Exception as e:
        return 500, {"message": str(e)}
    

""" To upload images"""
@api.post("/image")
def upload_image(request, alt_text: str = Form(...),
                description: str = Form(...),
                id: int = Form(...),
                file: UploadedFile = File(...)):
    
    qs = get_object_or_404(Post, id=id)
    media = Images.objects.create(
                                post=qs, alt_text=alt_text, 
                                description=description,
                                link = file)
    return {"message": "image has been successfully created"}




    
        

    

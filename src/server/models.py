from django.db import models
from django.contrib.auth.models import User

# class Images(models.Model):

#     # id = models.AutoField()
#     alt_text = models.CharField(max_length=255, blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     link = models.ImageField()

#     def __str__(self) -> str:
#         return self.alt_text
    
# def upload_to(instance, filename):
#     return f"images"

class Category(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):

    choices = (
          ("PUBLISED", "Published"),
          ("DRAFT", "Draft"),
     )
    # id = models.AutoField()
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,
                    on_delete=models.CASCADE)
    content = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=choices,
                              max_length=255, default="DRAFT")
    image = models.ImageField(upload_to="images", 
                              height_field=None, width_field=None,
                            max_length=100,
                              blank=True, null=True)

    category = models.ManyToManyField(Category)

    def __str__(self)-> str:
        return self.title
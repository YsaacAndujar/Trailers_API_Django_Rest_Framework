
from django.db import models

class Category(models.Model):
    name=models.TextField(max_length=30, unique=True)

class Trailers(models.Model):
    title = models.TextField(max_length=30),
    release_date = models.DateField(null=True),
    description=models.TextField(max_length=170),
    cast=models.TextField(max_length=50),
    image =models.ImageField(upload_to='media'),
    trailerUrl=models.TextField(max_length=15),
    category=models.ForeignKey(Category, null=True,on_delete=models.CASCADE)


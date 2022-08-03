from dataclasses import field, fields
from django.db import models
from django.forms import ModelForm, TextInput

class Category(models.Model):
    name=models.TextField(max_length=50, unique=True)

class Trailers(models.Model):
    title = models.TextField(max_length=70),
    release_date = models.DateField(null=True),
    description=models.TextField(max_length=200),
    cast=models.TextField(max_length=100),
    image =models.ImageField(upload_to='media'),
    trailerUrl=models.TextField(max_length=15),
    category=models.ForeignKey(Category, null=True,on_delete=models.CASCADE)

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            'name': TextInput(attrs={
				        'id':'category-name-input',
                    }),
        }

class TrailersForm(ModelForm):
    class Meta:
        model = Trailers
        fields = "__all__"
        widgets = {
            'title': TextInput(attrs={
				        'id':'title-input',
                    }),
        } 
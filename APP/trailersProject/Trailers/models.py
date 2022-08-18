from django import forms
from django.db import models
from django.forms import CheckboxSelectMultiple, DateInput, FileInput, ModelForm, ModelMultipleChoiceField, TextInput, Textarea

class Category(models.Model):
    name=models.TextField(max_length=50, unique=True)
    def __str__(self):
         return self.name

class Trailers(models.Model):
    title = models.TextField(max_length=70, verbose_name="Title")
    release_date = models.DateField(null=True, blank=True)
    description=models.TextField(max_length=700)
    cast=models.TextField(max_length=100)
    image =models.ImageField(upload_to='images', blank=True )
    trailerUrl=models.TextField(max_length=15)
    category = models.ManyToManyField(Category, blank=True)

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            'name': TextInput(attrs={
				        'id':'category-name-input',
                    }),
        }

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, category):
        return "%s" % category.name
        
class TrailersForm(ModelForm):
    class Meta:
        model = Trailers
        fields = "__all__"
        widgets = {
            'title': TextInput(
                attrs={
                    'id':'title-input',
                }
            ),
            'release_date': DateInput(

                attrs={
                    'type': 'date',
                    'id': 'release_date_input'
                },
            ),
            'cast': Textarea(
                attrs={
                    'id':'cast-input'
                }
            ),
            'description': Textarea(
                attrs={
                    'id':'description-input'
                }
            ),
            'trailerUrl': TextInput(
                attrs={
                    'id':'code',
                    'class':'ytcode-input'                    
                }
            ),
            'image': FileInput(
                attrs={
                    'id':'imageUpload',
                    'name':'imageUpload',
                    'class':'hide',
                }
            ),
            'category': CheckboxSelectMultiple(
                attrs={
                }
            )
        }     

        
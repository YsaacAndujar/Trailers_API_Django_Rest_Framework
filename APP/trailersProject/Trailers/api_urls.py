from django.urls import path
from . import api_views

urlpatterns = [
    path('categories/', api_views.CategoriesView.as_view()),
    path('preview-trailers/', api_views.previewTrailersView.as_view()),
    path('get-trailer/<int:pk>', api_views.getTrailerView.as_view()),
]
from django.urls import path

from . import views
app_name="Trailers"
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('add-trailer/', views.addTrailer, name="addTrailer"),
    path('view-trailers/', views.viewTrailers, name="viewTrailers"),
    path('modify-trailer/<int:pk>', views.modifyTrailer, name="modifyTrailer"),
    path('delete-trailer/<int:pk>', views.deleteTrailer, name="deleteTrailer"),
    path('add-category/', views.addCategory, name="addCategory"),
    path('delete-category/<int:pk>', views.deleteCategory, name="deleteCategory"),
    path('modify-category/<int:pk>', views.modifyCategory, name="modifyCategory"),
    path('view-categories/', views.viewCategories, name="viewCategories"),
]
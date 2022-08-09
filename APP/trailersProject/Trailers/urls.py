from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
app_name="Trailers"
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('add-trailer/', login_required(views.addTrailer), name="addTrailer"),
    path('view-trailers/', login_required(views.viewTrailers), name="viewTrailers"),
    path('modify-trailer/<int:pk>', login_required(views.modifyTrailer), name="modifyTrailer"),
    path('delete-trailer/<int:pk>', login_required(views.deleteTrailer), name="deleteTrailer"),
    path('add-category/', login_required(views.addCategory), name="addCategory"),
    path('delete-category/<int:pk>', login_required(views.deleteCategory), name="deleteCategory"),
    path('modify-category/<int:pk>', login_required(views.modifyCategory), name="modifyCategory"),
    path('view-categories/', login_required(views.viewCategories), name="viewCategories"),
]
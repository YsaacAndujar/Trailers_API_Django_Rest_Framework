from django.urls import path
from . import views
app_name="Trailers"
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('add/', views.add, name="add"),
]
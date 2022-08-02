from django.urls import path
from . import views
app_name="Trailers"
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('addTrailer/', views.addTrailer, name="addTrailer"),
    path('viewTrailers/', views.viewTrailers, name="viewTrailers"),
    path('addCategory/', views.addCategory, name="addCategory"),
]
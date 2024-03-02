from django.urls import path
from . import views


urlpatterns = [
    path ("",views.home,name="home"),
    path ("photo/<str:pk>",views.viewphoto,name="photo"),
    path ("add/",views.addphoto,name="add"),
]

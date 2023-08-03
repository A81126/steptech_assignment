from django.urls import path
from .views import *

urlpatterns = [
    
    path("",home),
    path("users",home),
    path("hello/",hello),
    path("new-user/",user_add),
    path("/users/<id>",user_search)
]
from django.urls import path
from .views import *

urlpatterns = [
    path('users/',Users.as_view()),
]
    
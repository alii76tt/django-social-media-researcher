from operator import index
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
]

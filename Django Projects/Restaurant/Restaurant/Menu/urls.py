from django.urls import path
from .views import *

urlpatterns = [
    path('menu', GetMenu.as_view()),
    path('addItem', AddItem.as_view()),
]
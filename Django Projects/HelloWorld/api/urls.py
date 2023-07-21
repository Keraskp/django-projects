from rest_framework.urls import path
from . import views

# create endpoints here

urlpatterns = [
    path('', views.getData),
]

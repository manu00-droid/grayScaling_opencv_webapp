from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cvt2gray/', views.cvt2gray),
]

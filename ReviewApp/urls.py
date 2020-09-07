from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', views.menu, name="menu"),
    path('reviews/', views.reviews, name="reviews"),
    path('write_review/', views.write_review, name="write_review"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
]

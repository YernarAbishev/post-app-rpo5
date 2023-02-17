from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('news/all/', views.allNews, name='allNews'),
    path('news/add/', views.addPost, name='addPost'),
    path('news/detail/<int:pk>/', views.postDetail, name='postDetail'),
    path('news/delete/<int:pk>/', views.deletePost, name='deletePost'),
    path('news/edit/<int:pk>/', views.editPost, name='editPost'),
]
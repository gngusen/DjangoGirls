from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='post'),
    path('<str:id>/', views.post_details, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
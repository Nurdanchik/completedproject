from django.urls import path
from .views import NewsListAPIView, NewsDetailAPIView

urlpatterns = [
    path('newslist/', NewsListAPIView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
]
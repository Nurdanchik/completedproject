from django.urls import path
from .views import RequestCreateAPIView

urlpatterns = [
    path('create-request/', RequestCreateAPIView.as_view(), name='create-request'),
]

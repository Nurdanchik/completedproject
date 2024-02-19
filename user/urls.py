from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserList, UserChange

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserChange.as_view(), name='user-change'),
]
from django.urls import path
from .views import RequestCreateAPIView, PaymentCreateAPIView

urlpatterns = [
    path('create-request/', RequestCreateAPIView.as_view(), name='create-request'),
    path('pay/', PaymentCreateAPIView.as_view(), name='pay'),
]

from rest_framework import generics
from .models import Request, Coupon
from rest_framework.views import APIView
import random
from rest_framework import serializers, status
import string
from datetime import date, timedelta
from rest_framework.response import Response
from .serializers import RequestSerializer, CouponSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from booking import settings
from tournaments.models import Tournament
import random 

class PaymentCreateAPIView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated] 

class RequestCreateAPIView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
from rest_framework import serializers
from .models import Request, Coupon

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['name', 'surname', 'phone_number', 'gmail', 'tournament', 'cupon']

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['cupon', 'valid', 'validuntil']


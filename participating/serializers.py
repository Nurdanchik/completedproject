from rest_framework import serializers
from .models import Request

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['name', 'surname', 'phone_number', 'gmail', 'tournament']

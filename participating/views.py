from rest_framework import generics
from .models import Request
from .serializers import RequestSerializer
from rest_framework.permissions import IsAuthenticated

class RequestCreateAPIView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
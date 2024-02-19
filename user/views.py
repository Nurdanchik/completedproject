from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegistrationSerializer, LoginSerializer

class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer

class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAdminUser]

class UserChange(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Обновление пароля
        if 'password' in request.data:
            instance.set_password(request.data['password'])
            instance.save()
        else:
            self.perform_update(serializer)

        return Response(serializer.data)

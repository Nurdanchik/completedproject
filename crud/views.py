from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from user.serializers import RegistrationSerializer
from tournaments.serializers import TournamentSerializer
from tournaments.models import Tournament
from news.models import News
from participating.serializers import RequestSerializer
from participating.models import Request
from news.serializers import NewsSerializer

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


        if 'password' in request.data:
            instance.set_password(request.data['password'])
            instance.save()
        else:
            self.perform_update(serializer)

        return Response(serializer.data)
    

class TournamentChange(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = [IsAdminUser]


class NewsChange(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]

class RequestsList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAdminUser]
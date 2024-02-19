from django.urls import path
from .views import UserList, UserChange, TournamentChange, NewsChange, RequestsList

urlpatterns = [
    path('crud/user/<int:pk>/', UserChange.as_view(), name='user-change'),
    path('crud/userslist', UserList.as_view(), name='user-list'),
    path('crud/tournamet/<int:pk>/', TournamentChange.as_view(), name='tournament-change'),
    path('crud/news/<int:pk>/', NewsChange.as_view(), name='news-change'),
    path('crud/requestslist', RequestsList.as_view(), name='requests-list'),
]
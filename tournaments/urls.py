from django.urls import path
from .views import TournamentListCreateView, TournamentDetailView
# , SearchTournamentView

urlpatterns = [
    path('tournamentslist/', TournamentListCreateView.as_view(), name='tournament-list-create'),
    path('tournaments/<int:pk>/', TournamentDetailView.as_view(), name='tournament-detail'),
    # path('tournaments/search', SearchTournamentView.as_view(), name='tournament-search'),
]
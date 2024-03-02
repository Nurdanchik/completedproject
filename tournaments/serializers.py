from rest_framework import serializers
from .models import Tournament
# , SearchTournament

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'name', 'picture', 'price_fund', 'whoisowner', 'price_for_participating', 'description', 'teamsallowed', 'date', 'alreadyin', 'formatt', 'sports', 'cyberSports', 'typee']

#     class Meta:
#         model = SearchTournament
#         fields = ['tosearch']
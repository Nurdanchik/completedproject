from django.contrib import admin
from .models import Tournament

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'whoisowner', 'time_for_registration_left')
    search_fields = ('description',)
    list_filter = ('time_for_registration_left',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        super().save_model(request, obj, form, change)

from django.contrib import admin
from .models import Pirate, Bounty

class BountyAdmin(admin.ModelAdmin):
    list_display = ('amount', 'amount_type')
    search_fields = ('amount',)

class PirateAdmin(admin.ModelAdmin):
    list_display = (
        'pirate_name', 'special_name', 'gender','position_in_crew',
        'devil_fruit_name', 'haki_type', 'spec_power', 'species',
        'current_bounty', 'age', 'date_of_birth', 'dream'
    )
    search_fields = ('pirate_name', 'special_name', 'position_in_crew', 'species')
    list_filter = ('gender', 'species', 'haki', 'devil_fruit')

admin.site.register(Bounty, BountyAdmin)
admin.site.register(Pirate, PirateAdmin)





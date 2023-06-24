from django.contrib import admin
from characters.models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'race',
    )

    list_display_links = (
        'id',
        'name'
    )
    search_fields = (
        'name',
        'race'
    )
    list_filter = (
        'name',
        'race'
    )

    list_per_page = 10

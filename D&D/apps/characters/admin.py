from django.contrib import admin
from characters.models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'raca',
    )

    list_display_links = (
        'id',
        'nome'
    )
    search_fields = (
        'raca',
        'nome'
    )
    list_filter = (
        'nome',
        'raca'
    )

    list_per_page = 10

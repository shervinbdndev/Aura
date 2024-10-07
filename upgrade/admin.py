from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CardUpgrade, Card




admin.site.unregister(Group)




@admin.register(Card)
class CardModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'icon']




@admin.register(CardUpgrade)
class CardUpgradeModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'card_name', 'card_level', 'card_upgrade_cost']
    search_fields = ['user__username', 'card_name']
    list_filter = ['card_level',]
    ordering = ['user', 'card_level']
    readonly_fields = ['card_upgrade_cost']
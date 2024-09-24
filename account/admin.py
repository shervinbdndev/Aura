from django.contrib import admin

from .models import UserCoinModel





class UserCoinModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'coins']
    search_fields = ['user__username',]
    list_filter = ['user',]
    ordering = ['-coins',]
    list_editable = ['coins',]
    
    


admin.site.register(UserCoinModel, UserCoinModelAdmin)
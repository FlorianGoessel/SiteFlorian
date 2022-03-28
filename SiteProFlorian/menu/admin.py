from django.contrib import admin
from .models import Sons


class SonsAdmin(admin.ModelAdmin):
    list_display = ('titre', 'cover', 'plugin', 'beatmaker', 'explicitcontent', 'date')
    search_fields = ['nom']


# Register your models here.
admin.site.register(Sons, SonsAdmin)
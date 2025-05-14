from django.contrib import admin
from .models import Page

@admin.register(Page)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'PageTitle', 'PageUrl', 'PagePriority', 'PageContent', 'currenttime']
    list_display_links = ['PageTitle', ]
    list_editable = ['PageUrl', 'PagePriority',]
    search_fields = ['PageContent',]
    list_filter = ['PageTitle', 'PageUrl']
    list_per_page = 15

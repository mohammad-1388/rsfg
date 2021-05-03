from django.contrib import admin
from RestFrameWork.models import Book

class AdminMode(admin.ModelAdmin):
    list_display = ['name', 'store_name', 'fav']
    search_fields = ['name', 'store_name']


admin.site.register(Book, AdminMode)

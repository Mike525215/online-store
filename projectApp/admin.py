from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']
    list_display_links = ['id']
    ordering = ['id']
    prepopulated_fields = {'slug': ('name',)}

class ItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_editable = ['title', 'price']
    list_display_links = ['id']
    ordering = ['id']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Favourites)
admin.site.register(Cart)


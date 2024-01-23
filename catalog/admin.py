from django.contrib import admin

from catalog.models import Blog


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('name', 'creation_at',)

from django.contrib import admin

from .models import Directions, Doctors


@admin.register(Directions)
class DirectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name', 'sort_number')
    list_filter = ('name', 'slug', 'sort_number')


@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'direction', 'work_experience', 'sort_number')
    search_fields = ('name', 'direction', 'work_experience')
    ordering = ('name', 'direction', 'sort_number', 'work_experience')
    list_filter = ('name', 'direction', 'slug', 'work_experience')

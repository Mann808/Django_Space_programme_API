from django.contrib import admin
from django.db import models
from .models import *
from django.http import HttpResponse
import csv

# Базовый класс
class BasePaginatedAdmin(admin.ModelAdmin):
    list_per_page = 3

    def logical_delete_selected(self, request, queryset):
        deleted_objects = queryset.filter(deleted=True)
        non_deleted_objects = queryset.filter(deleted=False)

        if deleted_objects.exists():
            deleted_objects.update(deleted=False)
            self.message_user(request, "Выбранные объекты успешно восстановлены.")
        else:
            non_deleted_objects.update(deleted=True)
            self.message_user(request, "Выбранные объекты успешно логически удалены.")
    logical_delete_selected.short_description = "Логически удалить/восстановить выбранные"

    def generate_csv_report(modeladmin, request, queryset):
        model_name = queryset.model.__name__

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{model_name}_report.csv"'

        writer = csv.writer(response)
        writer.writerow([field.name for field in queryset.model._meta.fields])

        for obj in queryset:
            writer.writerow([getattr(obj, field.name) for field in obj._meta.fields])

        return response

    generate_csv_report.short_description = "Создать отчет CSV"
    
    actions = ['logical_delete_selected', 'generate_csv_report']

# Регистрация моделей для административного интерфейса
@admin.register(Role)
class RoleAdmin(BasePaginatedAdmin):
    pass

@admin.register(User)
class UserAdmin(BasePaginatedAdmin):
    list_display = ('username', 'name', 'role', 'deleted')
    list_filter = ('role', 'deleted')
    search_fields = ['username', 'name']

@admin.register(SpaceMission)
class SpaceMissionAdmin(BasePaginatedAdmin):
    list_display = ('name', 'launch_date', 'deleted')
    list_filter = ('deleted', 'name')
    ordering = ('-launch_date',)
    search_fields = ['name', 'participating_countries']

@admin.register(Photo)
class PhotoAdmin(BasePaginatedAdmin):
    list_display = ('mission', 'object_type', 'capture_date', 'deleted')
    list_filter = ('deleted', 'object_type')
    ordering = ('capture_date',)
    search_fields = ['object_type']

@admin.register(Spacecraft)
class SpacecraftAdmin(BasePaginatedAdmin):
    list_display = ('name', 'launch_date', 'type', 'mission', 'deleted')
    list_filter = ('deleted', 'mission')
    ordering = ('name',)
    search_fields = ['name', 'type']

@admin.register(Galaxy)
class GalaxyAdmin(BasePaginatedAdmin):
    list_display = ('name', 'type', 'size', 'distance_from_earth', 'number_of_stars', 'has_black_hole', 'deleted')
    list_filter = ('deleted', 'has_black_hole')
    ordering = ('name',)
    search_fields = ['name', 'type']

@admin.register(Planet)
class PlanetAdmin(BasePaginatedAdmin):
    list_display = ('name', 'diameter', 'mass', 'average_distance_from_sun', 'orbital_period', 'number_of_moons', 'deleted')
    list_filter = ('deleted', 'galaxy')
    ordering = ('name',)
    search_fields = ['name']

@admin.register(Star)
class StarAdmin(BasePaginatedAdmin):
    list_display = ('name', 'spectral_class', 'surface_temperature', 'luminosity', 'distance_from_earth', 'galaxy', 'deleted')
    list_filter = ('deleted', 'galaxy')
    ordering = ('name',)
    search_fields = ['name', 'spectral_class']

@admin.register(Asteroid)
class AsteroidAdmin(BasePaginatedAdmin):
    list_display = ('name', 'diameter', 'mass', 'orbit', 'discovery_date', 'potential_hazard', 'galaxy', 'deleted')
    list_filter = ('deleted', 'galaxy')
    ordering = ('name',)
    search_fields = ['name', 'orbit']

@admin.register(BlackHole)
class BlackHoleAdmin(BasePaginatedAdmin):
    list_display = ('name', 'mass', 'distance_from_earth', 'galaxy', 'deleted')
    list_filter = ('deleted', 'galaxy')
    ordering = ('name',)
    search_fields = ['name']

@admin.register(FavoriteSpaceObject)
class FavoriteSpaceObjectAdmin(BasePaginatedAdmin):
    list_display = ('user', 'space_object_id', 'object_type', 'deleted')
    list_filter = ('deleted',)
    ordering = ('user', 'object_type')
    search_fields = ['object_type']

@admin.register(TicketStatus)
class TicketStatusAdmin(BasePaginatedAdmin):
    list_display = ('name', 'deleted')
    list_filter = ('deleted',)
    ordering = ('name',)
    search_fields = ['name']

@admin.register(Ticket)
class TicketAdmin(BasePaginatedAdmin):
    list_display = ('user', 'sale_date', 'number_of_tickets', 'status', 'deleted')
    list_filter = ('deleted',)
    ordering = ('sale_date',)
    search_fields = ['user__username']

@admin.register(TicketDetail)
class TicketDetailAdmin(BasePaginatedAdmin):
    list_display = ('ticket', 'passenger_name', 'price', 'departure_planet', 'destination_planet', 'deleted')
    list_filter = ('deleted', 'departure_planet')
    ordering = ('passenger_name',)
    search_fields = ['passenger_name']
    
from django.contrib import admin
from main.models import Town, Suburb, House, Agent, User


class MainAdminSite(admin.AdminSite):
    site_header = "Nyumbani Admin"
    site_title = site_header


class TownAdmin(admin.ModelAdmin):
    search_fields = ['name']


class SuburbAdmin(admin.ModelAdmin):
    list_display = ['name', 'town']
    search_fields = ['name', 'touwn']
    list_filter = ['town']


class HouseAdmin(admin.ModelAdmin):
    list_filter = ['location', 'agent', 'bedrooms', 'pets_allowed']
    list_display = ['name', 'location', 'agent', 'bedrooms']
    list_display_links = ['location', 'agent']
    search_fields = ['name', 'price', 'location', 'agent']


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number']
    search_fields = ['name', 'phone_number']


class AgentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number']
    search_fields = ['name', 'phone_number']


mainadmin = MainAdminSite(name='Nyumbani')
mainadmin.register(Town, TownAdmin)
mainadmin.register(Suburb, SuburbAdmin)
mainadmin.register(House, HouseAdmin)
mainadmin.register(Agent, AgentAdmin)
mainadmin.register(User, UserAdmin)

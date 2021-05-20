from django.contrib import admin

from .models import Client, Inventory, Mission, MissionResult

# Register your models here.
admin.site.register(Client)
admin.site.register(Inventory)
admin.site.register(Mission)
admin.site.register(MissionResult)
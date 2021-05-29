from django.contrib import admin
from .models import GeninNinja, ChuninNinja, JouninNinja, HokageNinja, Team

# Register your models here.
admin.site.register(GeninNinja)
admin.site.register(ChuninNinja)
admin.site.register(JouninNinja)
admin.site.register(HokageNinja)
admin.site.register(Team)
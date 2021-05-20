from django.contrib import admin

from .models import AttackSkill, HealSkill, Parchment

# Register your models here.
admin.site.register(AttackSkill)
admin.site.register(HealSkill)
admin.site.register(Parchment)

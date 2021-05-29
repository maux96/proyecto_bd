from django.contrib import admin

from .models import AttackSkill, HealSkill

# Register your models here.
admin.site.register(AttackSkill)
admin.site.register(HealSkill)

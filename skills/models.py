from django.db import models
from django.urls import reverse

# Create your models here.
class Skill(models.Model):
    #skill basic attribute
    name = models.CharField(max_length=200)
    chakra_required = models.IntegerField()
    belong_to_the_village = models.BooleanField()
    element = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def class_name(self):
        return "Generic Skill"
        
    def specific_type(self):
        types = [AttackSkill,HealSkill]
        specific_skill = self
        for type in types:
            try: 
                specific_skill=type.objects.get(pk=self.pk)
                break
            except: pass
        return specific_skill
        

class AttackSkill(Skill):
    #attackSkill basic attribute
    range = models.IntegerField()

    def get_absolute_url(self):
        return reverse('skills:attack_skill_detail', kwargs={'pk': self.pk})

    def class_name(self):
        return "Attack"
        

class HealSkill(Skill):
    #healSkill basic attribute
    speed = models.IntegerField()

    def get_absolute_url(self):
        return reverse('skills:heal_skill_detail', kwargs={'pk': self.pk})

    def class_name(self):
        return "Heal"

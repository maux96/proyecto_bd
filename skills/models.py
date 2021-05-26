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


class AttackSkill(Skill):
    #attackSkill basic attribute
    range = models.IntegerField()

    def get_absolute_url(self):
        return reverse('skills:attack_skill_detail', kwargs={'pk': self.pk})


class HealSkill(Skill):
    #healSkill basic attribute
    speed = models.IntegerField()

    def get_absolute_url(self):
        return reverse('skills:heal_skill_detail', kwargs={'pk': self.pk})


class Parchment(models.Model):
    #parchment basic attribute
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    date = models.DateField()
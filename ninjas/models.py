from django.db import models
from skills.models import Skill

# Create your models here.
class Ninja(models.Model):
    #ninja basic attribute
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    clan = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth')

    #ninja skill relationship
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name
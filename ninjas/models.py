from django.db import models
from skills.models import Skill
from invocations.models import Invocation

# Create your models here.
class Ninja(models.Model):
    #ninja basic attribute
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    clan = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth')
    gender = models.CharField(max_length=10)

    #ninja skill relationship
    skills = models.ManyToManyField(Skill)

    #ninja invocation relationship
    invocations = models.ManyToManyField(Invocation)

    def __str__(self):
        return self.name
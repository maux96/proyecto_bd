from django.db import models
from skills.models import Skill
from django.contrib.auth.models import User
from invocations.models import Invocation
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Team(models.Model):
    #team basic attribute
    name = models.CharField(max_length=200)
    in_mission = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Ninja(models.Model):
    #ninja basic attribute
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    clan = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth')
    gender = models.CharField(max_length=10)

    #ninja skill relationship
    skills = models.ManyToManyField(Skill, blank=True)

    #cuenta de django relacionada con ninja
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #ninja invocation relationship
    invocations = models.ManyToManyField(Invocation, blank=True)

    #ninja team relationship
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class GeninNinja(Ninja):
    graduation_date = models.DateField()
    assessment = models.IntegerField(default=5, validators=[MinValueValidator(0),MaxValueValidator(10)])


class ChuninNinja(Ninja):
    exam_date = models.DateField()
    classification = models.IntegerField(default=5, validators=[MinValueValidator(0),MaxValueValidator(10)])


class JouninNinja(Ninja):
    exam_date = models.DateField()
    classification = models.IntegerField(default=5, validators=[MinValueValidator(0),MaxValueValidator(10)])


class HokageNinja(Ninja):
    hokage_number = models.IntegerField()

    def __str__(self):
        return self.name + ",the " + str(self.hokage_number) + " Hokage of Konoha" 
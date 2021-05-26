from django.db import models
from skills.models import Skill
from django.contrib.auth.models import User
from invocations.models import Invocation
from django.core.validators import MinValueValidator, MaxValueValidator
from django.apps import apps

# Create your models here.
class Team(models.Model):
    #team basic attribute
    name = models.CharField(max_length=200)
    in_mission = models.BooleanField(default=False)
    
    def members(self):
        return Ninja.objects.filter(team_id=self.pk)

    def length(self):
        return len(self.members())

    def missions(self):
        return apps.get_model('missions','Mission').objects.filter(team_id=self.pk) #para que no se haga una importacion circular.

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

    def ninja_skills(self):
        return self.skills.all()
    def ninja_invocations(self):
        return self.invocations.all()
    def ninja_class(self):
        return type(self).__name__

    def __str__(self):
        return self.name



class GeninNinja(Ninja):
    graduation_date = models.DateField()
    assessment = models.IntegerField(default=5, validators=[MinValueValidator(0),MaxValueValidator(10)])
    def ninja_info(self):
        sol=[("Evaluacion",self.assessment),("Fecha de Graduacion",self.graduation_date)]
        return sol

class ChuninNinja(Ninja):
    exam_date = models.DateField()
    classification = models.IntegerField(default=5, validators=[MinValueValidator(0),MaxValueValidator(10)])
    def ninja_info(self):
        sol=[("Calificacion",self.classification),("Fecha del Examen",self.exam_date)]
        return sol

class JouninNinja(Ninja):
    exam_date = models.DateField()
    classification = models.IntegerField(default=5, validators=[MinValueValidator(0),MaxValueValidator(10)])
    def ninja_info(self):
        sol=[("Calificacion",self.calificlassificationcation),("Fecha del Examen",self.exam_date)]
        return sol
    """ def guide_of(self):
        return Team.objects.filter( guide_id = self.pk ) """

class HokageNinja(Ninja):
    hokage_number = models.IntegerField()

    def __str__(self):
        return self.name + ",the " + str(self.hokage_number) + " Hokage of Konoha" 
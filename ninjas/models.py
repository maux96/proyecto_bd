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
        return apps.get_model('missions','Mission').objects.filter(team_id=self.pk) 

    def __str__(self):
        return self.name


class Ninja(models.Model):
    #ninja basic attribute
    name = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=50,null=True,blank=True)
    age = models.IntegerField()
    clan = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth')
    gender = models.CharField(max_length=10)
    max_chakra = models.IntegerField(default=100,null=True,blank=True)

    is_medic = models.BooleanField(default=False)

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
    
    def class_name(self):
        return "Generic Ninja"
        
    def specific_type(self):
        types = [GeninNinja,ChuninNinja,JouninNinja,HokageNinja]
        specific_ninja = self
        for type in types:
            try: 
                specific_ninja=type.objects.get(pk=self.pk)
                break
            except: pass
        return specific_ninja

    def __str__(self):
        return self.name



class GeninNinja(Ninja):
    graduation_date = models.DateField()
    assessment = models.IntegerField(default=5, validators=[MinValueValidator(0),MaxValueValidator(10)])
    def ninja_info(self):
        sol=[("Assessment",self.assessment),("Graduation Date",self.graduation_date)]
        return sol
    
    def class_name(self):
        return "Genin"
        
class ChuninNinja(Ninja):
    exam_date = models.DateField()
    calification = models.IntegerField(default=5, validators=[MinValueValidator(0),MaxValueValidator(10)])
    def ninja_info(self):
        sol=[("Calification",self.calification),("Test Date",self.exam_date)]
        return sol

    def class_name(self):
        return "Chunin"
    
class JouninNinja(Ninja):
    exam_date = models.DateField()
    calification = models.IntegerField(default=5, validators=[MinValueValidator(0),MaxValueValidator(10)])
    leading_team = models.BooleanField(default=False, blank=True)
    
    def ninja_info(self):
        sol=[("Calification",self.calification),("Test Date",self.exam_date)]
        return sol
    
    def class_name(self):
        return "Jounin"
    
    """ def guide_of(self):
        return Team.objects.filter( guide_id = self.pk ) """

class HokageNinja(Ninja):
    hokage_number = models.IntegerField()

    def ninja_info(self):
        sol=[("Hokage Number",self.hokage_number)]
        return sol

    def __str__(self):
        return self.name + ",the " + str(self.hokage_number) + " Hokage of Konoha" 

    
    def class_name(self):
        return "Hokage"
    

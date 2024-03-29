from django.db import models
from ninjas.models import Team, JouninNinja
from skills.models import Skill
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Client(models.Model):
    #client basic attribute
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    #cuenta de django relacionada con cliente
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def missions(self):
        return Mission.objects.filter(client_id=self.pk )

    def __str__(self):
        return self.name


class Inventory(models.Model):
    #inventory basic attribute
    kunais = models.IntegerField(default=0)
    shurikens = models.IntegerField(default=0)
    explosive_seals = models.IntegerField(default=0)


class Parchment(models.Model):
    #parchment basic attribute
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    date = models.DateField()

    #Parchment Inventory relationship
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('missions:parchment_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.skill.name


class Mission(models.Model):
    #mission basic attribute
    name = models.CharField(max_length=200)
    description = models.TextField()
    rank = models.CharField(max_length=10)
    reward = models.IntegerField()
    available = models.BooleanField(default=True)

    #mission client relationship
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    #mission team relationship
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, blank=True,null=True)

    #mission inventory relationship
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE, default=None, null=True, blank=True)

    #mission jounin relationship
    leader = models.ForeignKey(JouninNinja, on_delete=models.CASCADE, default=None, blank=True,null=True)

    def missionResults(self):
        return MissionResult.objects.get(mission_id=self.pk)

    def __str__(self):
        return self.name


class MissionResult(models.Model):
    result = models.CharField(max_length=200)
    begin_date = models.DateField()
    end_date = models.DateField()

    #missionResult mission relationship
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)

    def __str__(self):
        return "("+str(self.pk)+") "+self.mission.name
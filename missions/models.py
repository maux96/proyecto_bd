from django.db import models
from ninjas.models import Team, JouninNinja
from skills.models import Parchment

# Create your models here.
class Client(models.Model):
    #client basic attribute
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    #inventory basic attribute
    kunais = models.IntegerField(default=0)
    shurikens = models.IntegerField(default=0)
    explosive_seals = models.IntegerField(default=0)

    #inventory parchment relationship
    parchment = models.OneToOneField(Parchment, on_delete=models.CASCADE, default=None, null=True)



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
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, blank=True)

    #mission inventory relationship
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE, default=None, null=True, blank=True)

    #mission jounin relationship
    leader = models.ForeignKey(JouninNinja, on_delete=models.CASCADE, default=None, blank=True)

    def __str__(self):
        return self.name


class MissionResult(models.Model):
    result = models.CharField(max_length=200)
    begin_date = models.DateField()
    end_date = models.DateField()

    #missionResult mission relationship
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
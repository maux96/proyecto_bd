from django.forms import Form, ModelMultipleChoiceField, ModelChoiceField
from django.forms.fields import CharField, IntegerField, BooleanField, DateField
from .models import Ninja, GeninNinja, ChuninNinja, JouninNinja, HokageNinja, Team
from missions.models import Mission, Parchment

class CreateTeamForm(Form):
    team_name = CharField(max_length=100)
    ninjas = ModelMultipleChoiceField(queryset=Ninja.objects.filter(team=None)
    .exclude(pk=HokageNinja.objects.all()[0].pk))


class AssignMissionForm(Form):
    mission = ModelChoiceField(queryset=Mission.objects.filter(available=True))
    team = ModelChoiceField(queryset=Team.objects.filter(in_mission=False))
    leader = ModelChoiceField(queryset=JouninNinja.objects.filter(leading_team=False, team=None))
    
    kunais = IntegerField()
    shurikens = IntegerField()
    explosive_seals = IntegerField()
    parchments = ModelMultipleChoiceField(queryset=Parchment.objects.filter(inventory=None), required=False)


class DeliverMissionResultForm(Form):
    success = BooleanField(required=False)
    begin_date = DateField()
    end_date = DateField()
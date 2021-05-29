from django.forms import Form, ModelMultipleChoiceField, ModelChoiceField,widgets
from django.forms.fields import CharField, IntegerField, BooleanField, DateField
from .models import Ninja, JouninNinja, Team
from missions.models import Mission, Parchment

class CreateTeamForm(Form):
    team_name = CharField(max_length=100)
    ninjas = ModelMultipleChoiceField(queryset=Ninja.objects.filter(team=None))
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        #agregarmos la clase de bootstrap       ver como no tener que hacer esto aqui....
        for x in self.fields:
            if isinstance(self.fields[x].widget, widgets.CheckboxInput):
                pass
            else:
                self.fields[x].widget.attrs['class']='form-control'

class AssignMissionForm(Form):
    mission = ModelChoiceField(queryset=Mission.objects.filter(available=True))
    team = ModelChoiceField(queryset=Team.objects.filter(in_mission=False))
    leader = ModelChoiceField(queryset=JouninNinja.objects.filter(leading_team=False, team=None))
    
    kunais = IntegerField()
    shurikens = IntegerField()
    explosive_seals = IntegerField()
    parchments = ModelMultipleChoiceField(queryset=Parchment.objects.filter(inventory=None), required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        #agregarmos la clase de bootstrap       ver como no tener que hacer esto aqui....
        for x in self.fields:
            if isinstance(self.fields[x].widget, widgets.CheckboxInput):
                pass
            else:
                self.fields[x].widget.attrs['class']='form-control'

class DeliverMissionResultForm(Form):
    success = BooleanField(required=False)
    begin_date = DateField()
    end_date = DateField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        #agregarmos la clase de bootstrap       ver como no tener que hacer esto aqui....
        for x in self.fields:
            if isinstance(self.fields[x].widget, widgets.CheckboxInput):
                pass
            else:
                self.fields[x].widget.attrs['class']='form-control'
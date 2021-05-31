from django.forms import ModelForm, RadioSelect, Form
from django.forms.fields import ChoiceField
from django.forms.models import ModelMultipleChoiceField
from django.forms.widgets import CheckboxInput
from .models import AttackSkill, HealSkill, Skill

class CreateAttackSkillForm(ModelForm):
    class Meta:
        model = AttackSkill
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        #agregarmos la clase de bootstrap       ver como no tener que hacer esto aqui....
        for x in self.fields:
            if isinstance(self.fields[x].widget, CheckboxInput):
                pass
            else:
                self.fields[x].widget.attrs['class']='form-control'

class CreateHealSkillForm(ModelForm):
    class Meta:
        model = HealSkill
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        #agregarmos la clase de bootstrap       ver como no tener que hacer esto aqui....
        for x in self.fields:
            if isinstance(self.fields[x].widget, CheckboxInput):
                pass
            else:
                self.fields[x].widget.attrs['class']='form-control'
class LearnSkillForm(Form):
    learn_skill = ModelMultipleChoiceField(queryset=Skill.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        #agregarmos la clase de bootstrap       ver como no tener que hacer esto aqui....
        for x in self.fields:
            if isinstance(self.fields[x].widget, CheckboxInput):
                pass
            else:
                self.fields[x].widget.attrs['class']='form-control'

from django.forms import ModelForm, RadioSelect, Form
from django.forms.models import ModelMultipleChoiceField
from .models import AttackSkill, HealSkill, Skill

class CreateAttackSkillForm(ModelForm):
    class Meta:
        model = AttackSkill
        fields = '__all__'
        choices = [('True', 'Yes'), ('False','No')]
        widgets = {
            'belong_to_the_village': RadioSelect(choices=choices),
        }


class CreateHealSkillForm(ModelForm):
    class Meta:
        model = HealSkill
        fields = '__all__'


class LearnSkillForm(Form):
    learn_skill = ModelMultipleChoiceField(queryset=Skill.objects.all())
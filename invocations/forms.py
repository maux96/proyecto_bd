from django.forms import ModelForm, Form
from django.forms.models import ModelMultipleChoiceField
from .models import Invocation

class CreateInvocationForm(ModelForm):
    class Meta:
        model = Invocation
        fields = '__all__'


class LearnInvocationForm(Form):
    learn_invocation = ModelMultipleChoiceField(queryset=Invocation.objects.all())
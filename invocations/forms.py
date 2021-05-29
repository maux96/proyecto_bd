from django.forms import ModelForm, Form
from django.forms.models import ModelMultipleChoiceField
from .models import Invocation

class CreateInvocationForm(ModelForm):
    class Meta:
        model = Invocation
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        #agregarmos la clase de bootstrap       ver como no tener que hacer esto aqui....
        for x in self.fields:
            self.fields[x].widget.attrs['class']='form-control'

class LearnInvocationForm(Form):
    learn_invocation = ModelMultipleChoiceField(queryset=Invocation.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        #agregarmos la clase de bootstrap       ver como no tener que hacer esto aqui....
        for x in self.fields:
            self.fields[x].widget.attrs['class']='form-control'

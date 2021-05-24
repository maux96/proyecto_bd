from typing import ClassVar
from django import forms
from django.db.models.fields import TextField
from django.forms import widgets

from .models import Client, Mission

class MyCharField(forms.CharField):
    widgets={
        'class':'form-control'
    }
    pass

"""         #eto ta weno       
class CreateMissionForm2(forms.ModelForm):
    class Meta:
        model= Mission
        exclude = ['client','team','inventory','leader']
        widgets = {
            'name':widgets.TextInput(attrs={'class':'form-control'}),
            'description':widgets.Textarea(attrs={'rows':3,'class':'form-control'}),
            'rank':widgets.TextInput(attrs={'class':'form-control'}),
            'reward':widgets.TextInput(attrs={'class':'form-control'}),
        } """

class CreateMissionForm(forms.Form):
    name = MyCharField(label="Mission Name",max_length=100) 
    description = forms.CharField(label="Description",max_length=500, widget=widgets.Textarea(attrs={'rows': 3}))
    rank = forms.CharField(label="Mission Rank",max_length=5)
    reward = forms.IntegerField(label="Mission Reward")
    #available = forms.BooleanField(label="Is Mission Available")

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        #agregarmos la clase de bootstrap       ver como no tener que hacer esto aqui....
        for x in self.fields:
            self.fields[x].widget.attrs['class']='form-control'
    
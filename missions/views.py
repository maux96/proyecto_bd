from django import forms
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.urls import reverse
from django.shortcuts import render,redirect
from django.views import generic

from .models import Client, Mission, Parchment
from .mission_form import CreateMissionForm, CreateParchmentForm

# Create your views here.
class ShowAllClientsView(generic.ListView):
    template_name = 'missions/show_all_clients.html'
    context_object_name = 'all_clients_list'
    paginate_by= 5
    def get_queryset(self):
        return Client.objects.all()

class ShowAllMissionsView(generic.ListView):
    template_name = 'missions/show_all_missions.html'
    context_object_name = 'all_missions_list'
    paginate_by = 5

    def get_queryset(self):
        return Mission.objects.all()

class MissionDetailView(generic.DetailView):
    model= Mission
    template_name = "missions/mission_details.html"

class ClientProfileView(generic.DetailView):
    model = Client
    template_name = "missions/profile.html"

class CreateParchmentView(generic.edit.CreateView):
    form_class = CreateParchmentForm
    template_name = 'missions/create_parchment.html'


class ParchmentDetailView(generic.DetailView):
    model = Parchment
    template_name = 'missions/parchment_detail.html'



def create_mission(request: HttpRequest):
    
    clients =Client.objects.filter( user_id = request.user.pk )
    if request.user.is_authenticated and len(clients):
        client = clients[0]
    else:
        return redirect('/auth/login')
        
    if request.method == 'POST':
        form = CreateMissionForm(request.POST)
        if form.is_valid():
            saveMission(request.POST,client)
            return redirect('missions:profile',client.pk)
        else:
            return render (request,reverse('missions:create_mission'),args={'form',form})
    else:    
        form=CreateMissionForm()
        return render(request,'missions/create_mission.html',{'form':form})


def saveMission(data,client):
    Mission(name = data['name'], description = data['description'],rank=data['rank'],reward = data['reward'],client = client).save()
    
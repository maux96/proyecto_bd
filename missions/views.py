from django.shortcuts import render
from django.views import generic

from .models import Client, Mission


# Create your views here.
class ShowAllClientsView(generic.ListView):
    template_name = 'missions/show_all_clients.html'
    context_object_name = 'all_clients_list'

    def get_queryset(self):
        return Client.objects.all()

class ShowAllMissionsView(generic.ListView):
    template_name = 'missions/show_all_missions.html'
    context_object_name = 'all_missions_list'

    def get_queryset(self):
        return Mission.objects.all()

class MissionDetailView(generic.DetailView):
    model= Mission
    template_name = "missions/mission_details.html"

class ClientProfileView(generic.DetailView):
    model = Client
    template_name = "missions/profile.html"
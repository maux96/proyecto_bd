import ninjas
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Ninja, Team

# Create your views here.

class ShowNinjaProfileView(LoginRequiredMixin, generic.DetailView):
    login_url = '/auth/login/'
    model = Ninja
    template_name = 'ninjas/profile.html'


class ShowAllNinjasView(generic.ListView):
    template_name = 'ninjas/show_all_ninjas.html'
    context_object_name = 'all_ninjas_list'

    def get_queryset(self):
        return Ninja.objects.all()

class ShowAllTeamsView(generic.ListView):
    template_name='ninjas/show_all_teams.html'
    context_object_name='all_teams_list'

    def get_queryset(self):
        return Team.objects.all()

class ShowNinjaSkillsView(generic.ListView):
    template_name = 'ninjas/show_ninja_skills.html'
    context_object_name = 'all_ninja_skills_list'

    def get_queryset(self):
        ninja = get_object_or_404(Ninja, pk=self.kwargs['pk'])
        return ninja.skills.all()


class ShowNinjaInvocationsView(generic.ListView):
    template_name = 'ninjas/show_ninja_invocations.html'
    context_object_name = 'all_ninja_invocations_list'

    def get_queryset(self):
        ninja = get_object_or_404(Ninja, pk=self.kwargs['pk'])
        return ninja.invocations.all()


class ShowNinjaTeamView(generic.DetailView):
    model = Ninja
    template_name = 'ninjas/show_ninja_team.html'


def ShowTeamView(request,pk):
    first_ninja_in_team=Team.objects.get(id=pk).members()[0]
    return  render(request,"ninjas/show_team.html",context={'ninja': first_ninja_in_team})


def ShowTeamMissionView(request, pk):
    team = get_object_or_404(Team, pk=pk)
    context = {}
    if team.in_mission:
        mission_in_progress = team.mission_set.all()[0]
        context = {'team': team, 'mission_in_progress':mission_in_progress }
    else:
        context = {'team':team}

    return render(request,'ninjas/show_team_mission.html',context)



"""
class ShowTeamMissionView(generic.ListView):
    template_name = 'ninjas/show_team_mission.html'
    context_object_name = 'mission_in_progress'

    def get_queryset(self):
        team_object = get_object_or_404(Team, pk=self.kwargs['pk'])
        return team_object.mission_set.all()[0]
"""

class ShowTeamMissionsView(generic.ListView):
    template_name = 'ninjas/show_team_missions.html'
    context_object_name = 'all_team_missions_list'

    def get_queryset(self):
        team_object = get_object_or_404(Team, pk=self.kwargs['pk'])
        return team_object.mission_set.all()
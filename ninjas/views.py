from django.db.models import Q
from django.http.request import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateTeamForm, AssignMissionForm, DeliverMissionResultForm
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Ninja, Team, JouninNinja
from missions.models import Inventory, Mission, MissionResult

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

    paginate_by=5
    
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


class CreateTeamView(generic.FormView):
    template_name = 'ninjas/create_ninja_team.html'
    form_class = CreateTeamForm

    def form_valid(self, form):
        
       # for n in form.cleaned_data['ninjas']:
       #     if n.is_medic:
        new_team = Team.objects.create(name=form.cleaned_data['team_name'])
        new_team.save()
        for ninja in form.cleaned_data['ninjas']:
            ninja.team = new_team
            ninja.save()
        #break

        return HttpResponseRedirect(reverse('ninjas:all'))

#Querys :)
class ShowNinjasQuerys(generic.ListView):
    template_name = "ninjas/show_ninja_query.html"
    context_object_name = "ninja_query"
    paginate_by = 5        
class ShowAllNinjasQuery(ShowNinjasQuerys):
    def get_queryset(self):
        return Ninja.objects.all()
class ShowNinjaTeamQuery(ShowNinjasQuerys):
    def get_queryset(self):
        team_pk =self.kwargs['team']
        return Ninja.objects.filter(team_pk = team_pk)
class ShowNinjaNameQuery(ShowNinjasQuerys):
    def get_queryset(self):
        name =self.kwargs['name']
        return Ninja.objects.filter(name__contains = name)
class ShowNinjasByGender(ShowNinjasQuerys):
    def get_queryset(self):
        gender = self.kwargs['gender']
        return Ninja.objects.filter(gender = gender)
class ShowNinjasByClan(ShowNinjasQuerys):
    def get_queryset(self):
        clan = self.kwargs['clan']
        return Ninja.objects.filter(clan__contains = clan)
class ShowNinjasByAge(ShowNinjasQuerys):
    def get_queryset(self):
        age = self.kwargs['age']
        return Ninja.objects.filter(age = age)
    
def filter(request : HttpRequest):
    value = request.POST['criteria']
    arg = request.POST['serach']
    return redirect(value+"/"+arg)


class DeliverMissionResultView(generic.FormView):
    template_name = 'ninjas/deliver_mission_result.html'
    form_class = DeliverMissionResultForm

    def form_valid(self, form):
        jounin = JouninNinja.objects.filter(pk=self.request.user.ninja.pk)[0]
        mission = jounin.team.mission_set.all()[jounin.team.mission_set.count()-1]
        team = jounin.team

        success = form.cleaned_data['success']
        if success:
            result = 'Success'
        else:
            result = 'Failure'   

        MissionResult.objects.create(result=result,
        begin_date=form.cleaned_data['begin_date'],
        end_date=form.cleaned_data['end_date'],
        mission=mission)

        team.in_mission = False
        team.save()
        jounin.leading_team = False
        jounin.team = None
        jounin.save()


        return HttpResponseRedirect(reverse('ninjas:show_all_ninjas'))



class AssignMissionView(generic.FormView):
    template_name = 'ninjas/assign_mission.html'
    form_class = AssignMissionForm

    def form_valid(self, form):
        mission = form.cleaned_data['mission'] 
        team = form.cleaned_data['team']
        leader = form.cleaned_data['leader']

        kunais = form.cleaned_data['kunais']
        shurikens = form.cleaned_data['shurikens']
        explosive_seals = form.cleaned_data['explosive_seals']
        parchments = form.cleaned_data['parchments']
        
        inventory = Inventory.objects.create(kunais=kunais,
        shurikens=shurikens,explosive_seals=explosive_seals)
        inventory.save()

        for parchment in parchments:
            parchment.inventory = inventory
            parchment.save()

        team.in_mission = True
        team.save()

        leader.leading_team = True
        leader.team = team
        leader.save()

        mission.team = team
        mission.leader = leader
        mission.available = False
        mission.inventory = inventory
        mission.save()


        return HttpResponseRedirect(reverse('ninjas:show_all_ninjas'))


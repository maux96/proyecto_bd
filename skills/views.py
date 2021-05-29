from django.shortcuts import render
from django.views import generic
from .models import Skill, AttackSkill, HealSkill
from .forms import CreateAttackSkillForm, CreateHealSkillForm, LearnSkillForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from itertools import chain
from django.db.models.query import QuerySet

# Create your views here.
class ShowAllSkillsView(generic.ListView):
    template_name = 'skills/show_all_skills.html'
    context_object_name = 'all_skills_list'

    paginate_by = 5
    
    def get_queryset(self):
        return Skill.objects.all()


class LearnSkillView(generic.FormView):
    template_name = 'skills/learn_skill.html'
    form_class = LearnSkillForm

    def form_valid(self, form):
        ninja = self.request.user.ninja
        for skill_form in form.cleaned_data['learn_skill']:
            ninja.skills.add(skill_form)            

        return HttpResponseRedirect(reverse('ninjas:profile', kwargs={'pk': self.request.user.ninja.pk}))


class AttackSkillDetail(generic.DetailView):
    model = AttackSkill
    template_name = 'skills/attack_skill_detail.html'


class HealSkillDetail(generic.DetailView):
    model = HealSkill
    template_name = 'skills/heal_skill_detail.html'


class CreateAttackSkillView(generic.edit.CreateView):
    form_class = CreateAttackSkillForm
    template_name = 'skills/create_attack_skill.html'


class CreateHealSkillView(generic.edit.CreateView):
    form_class = CreateHealSkillForm
    template_name = 'skills/create_heal_skill.html'


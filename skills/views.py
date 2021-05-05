from django.shortcuts import render
from django.views import generic
from .models import Skill

# Create your views here.
class ShowAllSkillsView(generic.ListView):
    template_name = 'skills/show_all_skills.html'
    context_object_name = 'all_skills_list'

    def get_queryset(self):
        return Skill.objects.all()
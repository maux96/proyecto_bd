from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Ninja

# Create your views here.
class ShowAllNinjasView(generic.ListView):
    template_name = 'ninjas/show_all_ninjas.html'
    context_object_name = 'all_ninjas_list'

    def get_queryset(self):
        return Ninja.objects.all()


class ShowNinjaSkillsView(generic.ListView):
    template_name = 'ninjas/show_ninja_skills.html'
    context_object_name = 'all_ninja_skills_list'

    def get_queryset(self):
        ninja = get_object_or_404(Ninja, pk=self.kwargs['pk'])
        return ninja.skills.all()
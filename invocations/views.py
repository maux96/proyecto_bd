from django.shortcuts import render
from django.views import generic
from .models import Invocation

# Create your views here.
class ShowAllInvocationsView(generic.ListView):
    template_name = 'invocations/show_all_invocations.html'
    context_object_name = 'all_invocations_list'

    def get_queryset(self):
        return Invocation.objects.all()
from django.shortcuts import render
from django.views import generic
from .models import Invocation
from .forms import CreateInvocationForm, LearnInvocationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class ShowAllInvocationsView(generic.ListView):
    template_name = 'invocations/show_all_invocations.html'
    context_object_name = 'all_invocations_list'

    paginate_by = 5
    def get_queryset(self):
        return Invocation.objects.all()


class InvocationDetail(generic.DetailView):
    model = Invocation
    template_name = 'invocations/invocation_detail.html'


class CreateInvocationView(generic.edit.CreateView):
    form_class = CreateInvocationForm
    template_name = 'invocations/create_invocation.html'


class LearnInvocationView(generic.FormView):
    template_name = 'invocations/learn_invocation.html'
    form_class = LearnInvocationForm

    def form_valid(self, form):
        ninja = self.request.user.ninja
        for invocation_form in form.cleaned_data['learn_invocation']:
            ninja.invocations.add(invocation_form)            

        return HttpResponseRedirect(reverse('ninjas:profile', kwargs={'pk': self.request.user.ninja.pk}))
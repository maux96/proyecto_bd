from django.urls import path

from . import views

urlpatterns = [
    path('allInvocations/', views.ShowAllInvocationsView.as_view(), name='show_all_invocations'),
]

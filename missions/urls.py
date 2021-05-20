from django.urls import path

from . import views

app_name = "missions"
urlpatterns = [
    path('allClients/', views.ShowAllClientsView.as_view(), name='show_all_clients'),
    path('allMissions/', views.ShowAllMissionsView.as_view(), name='show_all_missions'),
]

from django.urls import path

from . import views

app_name = "missions"
urlpatterns = [
    path('allClients/', views.ShowAllClientsView.as_view(), name='show_all_clients'),
    path('allMissions/', views.ShowAllMissionsView.as_view(), name='show_all_missions'),
    path('mission/<int:pk>', views.MissionDetailView.as_view() , name='mission_details'),
    path('client/<int:pk>', views.ClientProfileView.as_view() , name='profile'),
    path('createMission/',views.create_mission, name='create_mission'),
    path('createParchment/',views.CreateParchmentView.as_view(), name='create_parchment'),
    path('parchment/<int:pk>/',views.ParchmentDetailView.as_view(), name='parchment_detail'),
]

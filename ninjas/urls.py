from django.urls import path

from . import views

app_name = "ninjas"
urlpatterns = [
    path('<int:pk>/', views.ShowNinjaProfileView.as_view(), name='profile'),
    path('allNinjas/', views.ShowAllNinjasView.as_view(), name='show_all_ninjas'),
    path('allTeams/', views.ShowAllTeamsView.as_view(), name='show_all_teams'),
    path('ninjaSkills/<int:pk>/', views.ShowNinjaSkillsView.as_view(), name='show_ninja_skills'),
    path('ninjaInvocations/<int:pk>/', views.ShowNinjaInvocationsView.as_view(), name='show_ninja_invocations'),
    path('ninjaTeam/<int:pk>/', views.ShowNinjaTeamView.as_view(), name='show_ninja_team'),
    path('team/<int:pk>/', views.ShowTeamView , name='show_team'),
    path('teamMission/<int:pk>/', views.ShowTeamMissionView, name='show_team_mission'),
    path('teamMissions/<int:pk>/', views.ShowTeamMissionsView.as_view(), name='show_team_missions'),
]
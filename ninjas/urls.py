from django.urls import path

from . import views

urlpatterns = [
    path('allNinjas/', views.ShowAllNinjasView.as_view(), name='show_all_ninjas'),
    path('ninjaSkills/<int:pk>', views.ShowNinjaSkillsView.as_view(), name='show_ninja_skills'),
]

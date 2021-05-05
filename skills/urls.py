from django.urls import path

from . import views

urlpatterns = [
    path('allSkills/', views.ShowAllSkillsView.as_view(), name='show_all_skills'),
]

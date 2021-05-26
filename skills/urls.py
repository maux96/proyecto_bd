from django.urls import path

from . import views

app_name = 'skills'
urlpatterns = [
    path('allSkills/', views.ShowAllSkillsView.as_view(), name='show_all_skills'),
    path('attackSkillDetail/<int:pk>/', views.AttackSkillDetail.as_view(), name='attack_skill_detail'),
    path('healSkillDetail/<int:pk>/', views.HealSkillDetail.as_view(), name='heal_skill_detail'),
    path('createAttackSkill/', views.CreateAttackSkillView.as_view(), name='create_attack_skill'),
    path('createHealSkill/', views.CreateHealSkillView.as_view(), name='create_heal_skill'),
    path('learnSkill/', views.LearnSkillView.as_view(), name='learn_skill'),
]

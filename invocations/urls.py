from django.urls import path

from . import views

app_name = 'invocations'
urlpatterns = [
    path('allInvocations/', views.ShowAllInvocationsView.as_view(), name='show_all_invocations'),
    path('invocationDetail/<int:pk>/', views.InvocationDetail.as_view(), name='invocation_detail'),
    path('createInvocation/', views.CreateInvocationView.as_view(), name='create_invocation'),
    path('learnInvocation/', views.LearnInvocationView.as_view(), name='learn_invocation'),
]

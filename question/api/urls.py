from django.urls import path
from . import views


app_name = 'question'

urlpatterns = [
    path('questions/', views.QuestionListView.as_view(), name='questions_all_list'),
    path('questions/<pk>/', views.QuestionDetailView.as_view(), name='questions_all_detail'),
]
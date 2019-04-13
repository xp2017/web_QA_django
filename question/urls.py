from django.urls import path, include
from . import views


app_name = 'question'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('search/', include('haystack.urls')),
    path('hot/', views.question_hot, name='question_hot'),
    path('question/<int:id>', views.question_detail, name='question_detail'),
    path('post/', views.question_post, name='question_post'),
    path('article/', views.article_list, name='article_list'),
    path('article/<int:id>', views.article_detail, name='article_detail'),
    path('article/post', views.article_post, name='article_post'),
]

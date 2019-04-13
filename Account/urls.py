from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'Account'

urlpatterns = [
    #path('', question_list, name='home_page'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('password_change', auth_views.PasswordChangeView.as_view(), name='password_change'),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('users/<username>/activities', views.user_detail, name='user_detail'),
    path('users/<username>/following', views.following_detail, name='following_detail'),
    path('users/<username>/followers', views.follower_detail, name='followers_detail'),

    ]
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('<username>/', views.profile, name='profile'),

]

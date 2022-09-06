from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUsr, name='login'),
    path('login/', views.loginUsr, name='login'),
    path('logout/', views.logoutFunc, name='logout'),
    path('signup/', views.signUp, name='signup'),
]
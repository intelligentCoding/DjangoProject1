from django.urls import path

from . import views

urlpatterns = [
    # home page
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    #Strona logowania
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name='login'),
    #Strona wylogowania
    path(r'^logout/$', views.logout_view, name='logout'),
]
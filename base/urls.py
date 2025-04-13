from django.urls import path
from . import views 
from django.urls import path
from .views import powerbi_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name="home"),
    path('signup/', views.signup_view, name="signup"),
    path('powerbi/', powerbi_view, name='powerbi'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile_view, name='profile'),

   
]

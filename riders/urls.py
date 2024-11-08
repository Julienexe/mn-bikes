from django.urls import path

from . import views

app_name="riders"
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signUp, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.riderDashboard, name='dashboard'),
    path('update_lease/', views.update_lease, name='update_lease'),
    path('about/', views.about, name='about'),
]
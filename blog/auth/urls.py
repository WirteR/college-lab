from django.urls import path

from . import views 

urlpatterns = [
    path('', views.main, name='main_auth'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('validate_register_data/', views.register, name='validate_register_data'),
    path('validate_auth_data/', views.login_view, name='validate_login_data'),
    path('logout/', views.logout_view, name='logout')
]
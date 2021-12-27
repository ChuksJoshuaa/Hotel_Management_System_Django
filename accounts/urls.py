from django.urls import path
from . import views


urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('manager_login/', views.manager_login, name='manager_login'),
    path('manager_signup/', views.manager_signup, name='manager_signup'),
    path('logout/', views.logout, name='logout')
]
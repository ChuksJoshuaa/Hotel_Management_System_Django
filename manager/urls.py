from django.urls import path
from . import views


urlpatterns = [
    path('manager/dashboard/', views.dashboard, name='manager_dashboard'),
    path('manager/add/', views.add_room, name='add-room'),
    path('manager/add-room/update/<int:room_no>/', views.update_room, name="update-room"),
]
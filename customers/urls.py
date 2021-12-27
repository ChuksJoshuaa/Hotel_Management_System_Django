from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.user_dashboard, name='user_dashboard'),
    path('detail/<int:id>/<int:booking_id>/', views.user_detail, name='user-detail')
]
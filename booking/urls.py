from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact-view'),
    path('book/', views.book_view, name='book'),
    path('book_now/<int:id>/', views.book_now, name='book_now'),
    path('book_confirm/', views.book_confirm, name='book-confirm'),
    path('cancel_room/<int:id>/', views.CancelRoom.as_view(), name='cancel'),
    path('room-delete/<int:id>/', views.DeleteRoom.as_view(), name='room-delete'),
]
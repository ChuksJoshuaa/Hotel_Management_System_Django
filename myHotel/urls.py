"""myHotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Hotel Admin'
admin.site.index_title = 'Manager Admin page'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('booking.urls')),
    path('api/', include('api.urls')),
    path('customers/', include('customers.urls')),
    path('', include('manager.urls')),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
          name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
          name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
          name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
          name='password_reset_complete'),
    path('__debug__/', include(debug_toolbar.urls)),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

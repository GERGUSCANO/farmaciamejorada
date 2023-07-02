"""
URL configuration for farmacia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from app_farmacia.views import SuperAdminRegistrationView, AdminRegistrationView, UserRegistrationView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app_farmacia.urls')),
    #path('accounts/', include('rest_registration.api.urls')),
    #path('register/superadmin/', SuperAdminRegistrationView.as_view(), name='superadmin-registration'),
    #path('register/admin/', AdminRegistrationView.as_view(), name='admin-registration'),
    #path('register/user/', UserRegistrationView.as_view(), name='user-registration'),
    #path('login/', LoginView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),
]



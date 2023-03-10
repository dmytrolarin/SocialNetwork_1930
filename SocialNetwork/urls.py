"""SocialNetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from registrationapp.views import *
from forum.views import *
from SocialNetwork import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg_form/', show_reg_form),
    path('reg_success/', show_reg_success, name = "reg_success"),
    path('login/', show_login_form, name = 'login'),
    path('welcome/',welcome, name = "welcome"),
    path('logout/',user_logout, name = "logout"),
    path('forum/', show_forum, name = 'forum'),
]

# Задаємо URL-адресу для медіа-файлів
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
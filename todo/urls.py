"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from core.views import create_task, user_signup, user_login, user_logout, redirect_to_main_page, deleting_task, editing_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_main_page, name='redirecting'),
    path('home/', create_task, name='home'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('edit/<int:srno>', editing_task, name='edit'),
    path('delete/<int:srno>', deleting_task, name='delete'),
]

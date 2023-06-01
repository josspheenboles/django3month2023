"""
URL configuration for todolist project.

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
from django.urls import path,include
from task.views import *
from myaccount.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Tasks/',include('task.urls')),
    #route for my account app
    path('List',userlist,name='userlist'),
    path('',Login,name='Login'),
    path('Logout',Logout,name='Logout'),
    path('Registration',Registration,name='Registration'),
    path('RegistrationAdmin',RegistrationAdmin,name='RegistrationAdmin'),
    path('RegistrationAdminModel',RegistrationAdminModel,name='RegistrationAdminModel'),
    #route for catagory app
    path('Catagory/',include('catagory.urls')),


]

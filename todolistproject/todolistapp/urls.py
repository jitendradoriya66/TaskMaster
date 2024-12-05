"""
URL configuration for todolistproject project.

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
from todolistapp.views import *


urlpatterns = [
path('create',create,name='create'),
path('',home,name='home'),

path('update/<int:id>',update,name='update'),
path('check/<int:id>',check,name='check'),

# path('update',update,name='update'),

path('delete_task/<int:id>',delete_task,name='delete_task'),

]
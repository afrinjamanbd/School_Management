"""School_Management URL Configuration

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
from django.urls import path, include
from administrator import views as administratorViews
from schoolsite import views as schoolsiteViews

urlpatterns = [
    path('admin/', admin.site.urls), #127.0.0.1:8000/admin
    path('rule/studentrules/<int:a>', administratorViews.rules, name = 'rules'), #127.0.0.1:8000/rule/studentrules
    path('administrator/<str:mystr>', include("administrator.urls")), #127.0.0.1:8000/administrator/dfbd/home  #127.0.0.1:8000/administrator/dfbd #127.0.0.1:8000/administrator/dfbd/profile #127.0.0.1:8000/administrator/dfbd/invoiceinfo
    # path('schoolsite/', include("schoolsite.urls")),
    path('facultynstaff/<slug:fs>',  schoolsiteViews.facultyStaff, {'settingvar':3})
    # path('teachersite/', include("teachersite.urls")),   
]

# 127.0.0.1:8000/facultynstaff/cdsj_ncs12-dvd
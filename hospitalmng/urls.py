"""hospitalmng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',About,name= 'about'),
    path('contact/',Contact,name= 'contact'),
    path('', Index, name='home'),
    path('admin_login/', Login, name='login'),
    path('logout/', Logout_admin, name='logout'),
    path('view_doctor/',View_doctor, name='view_doctor'),
    path('add_doctor/',Add_doctor, name='add_doctor'),
    path('delete_doctor(?p<int:pid>)/',Delete_doctor, name='Delete_doctor'),
    path('view_patient/',View_Patient, name='view_patient'),
    path('add_patient/',Add_Patient, name='add_patient'),
    path('delete_patient(?p<int:rid>)/',Delete_Patient, name='Delete_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),
    path('delete_appointment(?p<int:rid>)/', Delete_Appointment, name='Delete_appointment'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

]

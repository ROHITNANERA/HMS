"""HMSWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    # path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('addhostel/',views.addhostel,name='addhostel'),
    path('viewhostels/',views.viewhostel,name='viewhostels'),
    path('updatehostel/',views.updatehostel,name='updatehostel'),
    # path('select/',views.select,name='select'),
    path('updatehosteldata/',views.updatehosteldata,name='updatehosteldata'),
    path('addroom/',views.addroom,name='addroom'),
    path('saveroom/',views.saveroom,name='saveroom'),
    path('selecthostel/',views.selecthostel,name='selecthostel'),
    path('selecthostel/viewrooms/',views.viewrooms,name='viewrooms'),
    path('deleteroom/',views.deleteroom,name='deleteroom'),
    path('home/',views.selectforall,name='selectforall'),
    path('addfacility/',views.addfacility_form,name='addfacilityform'),
    path("savefacility/",views.addfacility,name="savefacility"),
    path("viewfacility/",views.viewfacilities,name="viewfacility"),
    path("deletefacility/",views.deletefacility,name="deletefacility"),
    path("viewstudents/",views.viewstudents,name="viewstudents"),
    path("deletestudents/",views.deletestudent,name="deletestudent"),
    path("addstudent/",views.addstudent,name="addstudent"),
    path("savestudent/",views.savestudent,name="savestudent"),
    path('updatestudent/',views.updatestudent,name="updatestudent")
    

]

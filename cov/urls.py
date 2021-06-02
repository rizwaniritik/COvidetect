from django.contrib import admin
from django.urls import path
from cov import views

urlpatterns = [
   path("",views.home,name="home"),
   path("/",views.home,name="home"),
  

]
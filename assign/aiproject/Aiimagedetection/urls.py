
from django.urls import path
from Aiimagedetection import views

urlpatterns = [

    path('', views.home,name="home"),
    path('report/',views.report,name="report"),
    
]
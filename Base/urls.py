from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('portfolio/', views.Portfolio, name="portfolio"),
    path('contact/', views.Contact, name="contact"),
    path('resume/', views.Resume, name="resume"),
    path('services/', views.Services, name="services"),
    path('about/', views.About, name="about"),
    path('confirmation/', views.Confirmation, name="confirmation"),
    path('portfolio-details/', views.Portfolio_details, name="portfolio-details"),
    path('service-details/', views.Service_details, name="service-details"),
    path('download-file/', views.Download_file, name="download-file"),

    

]



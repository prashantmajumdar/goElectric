from django.contrib import admin
from django.urls import path
from goElectricApp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('cars', views.cars, name="cars"),
    path('car-details', views.carsDetails, name="car-details"),
    path('contact', views.contact, name="contact"),
    path('blog', views.blog, name="blog"),
    path('about', views.about, name="about"),
    path('teams', views.teams, name="teams"),
    path('team', views.team, name="team"),
    path('testimonial', views.testimonial, name="testimonial"),
]

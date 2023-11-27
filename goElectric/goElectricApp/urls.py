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
    path('terms', views.terms, name="terms"),
    path('privacy-policy', views.privacypolicy, name="privacy-policy"),
    path('team', views.team, name="team"),
    path('testimonial', views.testimonial, name="testimonial"),
    path('login', views.userLogin, name="login"),
    path('registration', views.registration, name="registration"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('car-details/TataNexonEv', views.TataNexonEv, name="car-details/TataNexonEv"),
    path('car-details/kia', views.kia, name="kia"),
    path('car-details/bmw-i7', views.bmwi7, name="bmw-i7"),
    path('car-details/TataTiagoEV', views.TataTiagoEV, name="TataTiagoEV"),
    # dashboard paths
    path('dashboard/auth/sign-up.html', views.signup, name="signup"),
    path('dashboard/auth/sign-in.html', views.signin, name="signin"),
    path('dashboard/auth/confirm-mail.html', views.confirmmail, name="confirmmail"),
    path('dashboard/auth/lock-screen.html', views.lockscreen, name="lockscreen"),
    path('dashboard/auth/recoverpw.html', views.recoverpw, name="recoverpw"),
    path('dashboard/app/user-profile.html', views.userprofile, name="userprofile"),
    path('dashboard/app/user-add.html', views.useradd, name="useradd"),
    path('dashboard/app/user-list.html', views.userlist, name="userlist"),
    path('dashboard/app/user-privacy-setting.html', views.userprivacysetting, name="userprivacysetting"),
    path('dashboard/errors/error404.html', views.error404, name="error404"),
    path('dashboard/errors/error500.html', views.error500, name="error500"),

]

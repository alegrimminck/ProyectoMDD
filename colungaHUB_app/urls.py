from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.homepage, name="homepage"),
    #path('login', views.login),
    path('', include("django.contrib.auth.urls")),
    path('member-main', views.member_main),
    path('logout',views.logout),
]

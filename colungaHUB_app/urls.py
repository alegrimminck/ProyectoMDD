from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.main),
    path('login', views.login),
    path('member-main', views.member_main),
]

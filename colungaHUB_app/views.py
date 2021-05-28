from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
from django.contrib.auth import logout
from .models import *
# Create your views here.
def homepage(request):
  return render(request, 'index.html')

def login(request):
  return render(request, 'login.html')

def member_main(request):
  organizaciones = Organizacion.objects.all()
  context = {'organizaciones': organizaciones}
  return render(request, 'card.html', context)

def logout_path(request):
  logout(request)
  return redirect('/')
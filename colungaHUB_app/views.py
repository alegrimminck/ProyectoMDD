from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
from django.contrib.auth import logout

# Create your views here.
def homepage(request):
  return render(request, 'index.html')

def login(request):
  return render(request, 'login.html')

def member_main(request):
  return render(request, 'card.html')

def logout(request):
  logout(request)
  return redirect("homepage")
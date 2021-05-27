from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static

# Create your views here.
def main(request):
  return render(request, 'index.html')

def login(request):
  return render(request, 'login.html')

def member_main(request):
  return render(request, 'card.html')
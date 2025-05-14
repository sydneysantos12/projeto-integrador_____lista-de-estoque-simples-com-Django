from django.shortcuts import render
from django.http import HttpResponse
# from django

# Create your views here.

def home(request):
    return render(request, 'lista/index.html')
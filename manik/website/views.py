from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Subject
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib import messages
from manik.settings import BASE_DIR

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'index.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def _404_error(request):
    return render(request, '404.html')

def courses(request):
    return render(request, 'courses.html')

def subjectpages(request):
    return render(request, 'subjectpages.html')

def contact(request):
    return render(request, 'contact.html')
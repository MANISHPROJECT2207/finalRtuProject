from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Subject
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib import messages
from manik.settings import BASE_DIR
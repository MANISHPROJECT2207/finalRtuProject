from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Subject
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib import messages
from manik.settings import BASE_DIR
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

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
    items = Item.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'subjectpages.html', {
        'items' : items,
        'subjects' : subjects
    })

def contact(request):
    return render(request, 'contact.html')

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    if request.method == 'POST':
        x = request.POST.get('ue')
        password = request.POST.get('password')
        user = authenticate(request, username=x, password=password)
        if user is None:
            user = authenticate(request, email=x, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
            
    return render(request, 'signin.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pswd = request.POST.get('password')
        p2 = request.POST.get('p2')
        username = request.POST.get('username')
        
        if pswd != p2:
            return redirect('register')

        try:
            user = User.objects.create_user(email=email, password=pswd, username=username)
            user.save()
        except Exception as e:
            return redirect('register')

        # Attempt to authenticate the user
        user = authenticate(request, email=email, password=pswd)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    return render(request, 'register.html')

def logout_user(request):
    logout(request)
    return redirect('home')


def search(request):
    items = Item.objects.all()
    query = request.GET.get('query', '')
    subjects = Subject.objects.all()
    if query:
        items = items.filter(Q(description__icontains=query) | Q(title__icontains=query))
        subjects = subjects.filter(Q(name__icontains=query) | Q(branch__icontains=query))
    return render(request, 'subjectpages.html', {
        'items': items,
        'subjects': subjects,
        'query': query,
    })
    
    
@csrf_exempt
@require_POST
def status_completed(request):
    
    data = json.loads(request.body)
    item_id = data.get('item_id')
    
    try:
        item = Item.objects.get(id=item_id)
        item.status = "completed"  # Assuming 'completed' is a valid status
        item.save()
        return JsonResponse({'success': True})
    except Item.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
    
def revision(request):
    subjects = Subject.objects.all()
    items = Item.objects.all().filter(revision='revision')
    a = Subject.objects.all().filter(year = 1)
    b = Subject.objects.all().filter(year = 2)
    c = Subject.objects.all().filter(year = 3)
    d = Subject.objects.all().filter(year = 4)
    g = Subject.objects.all().filter(year = 0)
    return render(request, 'subjectpages.html', {'items':items, 'subjects': subjects,
        'a':a, 'b':b, 'c':c, 'd':d, 'g':g
    })
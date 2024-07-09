from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('_404_error/', views._404_error, name='_404_error'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('subjectpages/', views.subjectpages, name='subjectpages'),
    path('testimonial/', views.testimonial, name='testimonial'),
]

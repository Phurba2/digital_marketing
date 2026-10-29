from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('lesson/<int:lesson_id>/toggle/', views.toggle_progress, name='toggle_progress'),
    path('register/', views.register, name='register'),
]

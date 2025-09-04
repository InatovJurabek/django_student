from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from .views import RegisterView 

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('api/teachers/', views.teacher_list_create, name='teacher_list_api'),
    path('api/students/', views.student_list_create, name='student_list_create'),
    path('api/courses/', views.course_list_create, name='course_list_create'),
    path('register/', RegisterView.as_view(), name='register'),
]


from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from main.models import Teacher, Student, Course
from users.serializers import TeacherSerializer, StudentSerializer, CourseSerializer


@api_view(['GET'])
def teacher_list_create(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def student_list_create(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def course_list_create(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)




def user_login_view(request):
    if request.method == 'GET':
        return render (request, 'users/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username,
                        password = password)
    if user is not None:
        login(request, user)
        return redirect('subject_list')
    else:
        return redirect('login')
    


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
    
    

    

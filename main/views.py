from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Teacher, Student, Course, Enrollment
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['name', 'subject']
    template_name = 'teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['name', 'subject']
    template_name = 'teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher_list')



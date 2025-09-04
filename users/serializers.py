from rest_framework import serializers
from main.models import Teacher, Student, Course


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)  
    students = StudentSerializer(many=True, read_only=True)  

    class Meta:
        model = Course
        fields = '__all__'
        
        

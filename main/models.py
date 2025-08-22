from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) # Agar tavsif bo'lishi shart bo'lmasa
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    class Meta:
        ordering = ['name']
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True) # Email noyob bo'lishi kerak
    courses = models.ManyToManyField(Course, through='Enrollment', related_name='students')

    class Meta:
        ordering = ['name']
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_date = models.DateField(auto_now_add=True)

    class Meta:
        # Bir talaba bir kursga qayta yozila olmaydi
        unique_together = ('student', 'course')
        ordering = ['-enrolled_date'] # Yangi yozilganlar tepad turadi

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"

# from django.db import models

# class Teacher(models.Model):
#     name = models.CharField(max_length=100)
#     subject = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name

# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)

#     enrolled_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student.name} - {self.course.name}"






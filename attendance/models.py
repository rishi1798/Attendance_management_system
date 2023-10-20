from django.db import models

class Users(models.Model):
    
    typee = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Departments(models.Model):
    
    department_name = models.CharField(max_length=255)
    submitted_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.department_name} by {self.submitted_by}' 

class Students(models.Model):
    
    full_name = models.CharField(max_length=255)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    classs = models.CharField(max_length=255)
    submitted_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name} of {self.department}'

class Courses(models.Model):
    
    course_name = models.CharField(max_length=255)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    semester = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    lecture_hours = models.PositiveIntegerField()
    submitted_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.course_name} by {self.submitted_by}'

class AttendanceLog(models.Model):
    
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    present = models.BooleanField()
    submitted_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student} is {self.present}'

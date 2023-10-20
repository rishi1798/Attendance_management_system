from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersListAV.as_view(), name='users-list-create'),
    path('users/<int:pk>/', views.UserDetailsAV.as_view(), name='users-get-update'),

    path('departments/', views.DepartmentsListAV.as_view(), name='departments-list-create'),
    path('departments/<int:pk>/', views.DepartmentDetailAV.as_view(), name='departments-get-update'),

    path('students/', views.StudentsListAV.as_view(), name='students-list-create'),
    path('students/<int:pk>/', views.StudentsDetailAV.as_view(), name='student-get-update'),

    path('courses/', views.CoursesListAV.as_view(), name='courses-list-create'),
    path('courses/<int:pk>/', views.CoursesDetailAV.as_view(), name='course-get-update'),

    path('attendance-log/', views.AttendanceLogAV.as_view(), name='attendance-log-list-create'),
    path('attendance-log/<int:pk>/', views.AttendanceLogDetailAV.as_view(), name='attendance-get-update'),
]

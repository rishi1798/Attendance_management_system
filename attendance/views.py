from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users, Departments, Students, Courses, AttendanceLog
from .serializers import UsersSerializer, DepartmentsSerializer, StudentsSerializer, CoursesSerializer, AttendanceLogSerializer
from rest_framework.permissions import IsAuthenticated



class UsersListAV(APIView):
    
    permission_classes=[IsAuthenticated]

    def get(self,request):
        try:
            queryset = Users.objects.all()
        except Users.DoesNotExist:
            return Response({'error':"No user found"},status=status.HTTP_404_NOT_FOUND)

        serializer=UsersSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer  = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    
class UserDetailsAV(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response({'error':"No user found"},status=status.HTTP_404_NOT_FOUND)

        serializer = UsersSerializer(user,context={'request': request})
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response({'error':"No user found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=UsersSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error":"Data invalid format"},status=status.HTTP_400_BAD_REQUEST)

            


class DepartmentsListAV(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request):
        try:
            queryset = Departments.objects.all()
        except Departments.DoesNotExist:
            return Response({'error':"No deapartment found"},status=status.HTTP_404_NOT_FOUND)

        serializer=DepartmentsSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer  = DepartmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class DepartmentDetailAV(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        try:
            department = Departments.objects.get(pk=pk)
        except Departments.DoesNotExist:
            return Response({'error':"No deapartment found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=DepartmentsSerializer(department)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            department = Departments.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response({'error':"No user found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=DepartmentsSerializer(department,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error":"Data invalid format"},status=status.HTTP_400_BAD_REQUEST)




class StudentsListAV(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request):
        try:
            queryset = Students.objects.all()
        except Students.DoesNotExist:
            return Response({'error':"No deapartment found"},status=status.HTTP_404_NOT_FOUND)

        serializer=StudentsSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer  = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class StudentsDetailAV(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        try:
            student = Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            return Response({'error':"No student found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=StudentsSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            student = Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            return Response({'error':"No student found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=StudentsSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error":"Data invalid format"},status=status.HTTP_400_BAD_REQUEST)



class CoursesListAV(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request):
        try:
            queryset = Courses.objects.all()
        except Courses.DoesNotExist:
            return Response({'error':"No Courses found"},status=status.HTTP_404_NOT_FOUND)

        serializer=CoursesSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer  = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)



class CoursesDetailAV(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        try:
            queryset = Courses.objects.get(pk=pk)
        except Courses.DoesNotExist:
            return Response({'error':"No course found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=CoursesSerializer(queryset)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            queryset = Courses.objects.get(pk=pk)
        except Courses.DoesNotExist:
            return Response({'error':"No course found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=CoursesSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error":"Data invalid format"},status=status.HTTP_400_BAD_REQUEST)
    

class AttendanceLogAV(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request):
        try:
            queryset = AttendanceLog.objects.all()
        except AttendanceLog.DoesNotExist:
            return Response({'error':"No attandance found"},status=status.HTTP_404_NOT_FOUND)

        serializer=AttendanceLogSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer  = AttendanceLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class AttendanceLogDetailAV(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        try:
            queryset = AttendanceLog.objects.get(pk=pk)
        except AttendanceLog.DoesNotExist:
            return Response({'error':"No attendance found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=AttendanceLogSerializer(queryset)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            queryset = AttendanceLog.objects.get(pk=pk)
        except AttendanceLog.DoesNotExist:
            return Response({'error':"No attendance found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=AttendanceLogSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error":"Data invalid format"},status=status.HTTP_400_BAD_REQUEST)


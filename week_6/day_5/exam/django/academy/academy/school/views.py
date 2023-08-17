from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Teacher
from .serializers import CourseSerializer, TeacherSerializer

# Create your views here.
class course_details(APIView):
    
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

class teacher_list(APIView):
    
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
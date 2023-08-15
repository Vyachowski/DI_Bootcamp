from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from django.utils import timezone


# Create your views here.
class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        date_joined_param = self.request.query_params.get('date_joined')

        if date_joined_param:
            try:
                date_joined = timezone.datetime.strptime(date_joined_param, '%Y-%m-%d')
                queryset = queryset.filter(date_joined__date=date_joined.date())
            except ValueError:
                pass

        return queryset


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

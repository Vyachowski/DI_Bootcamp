from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department, Employee, Project, Task
from .serializers import DepartmentSerializer, EmployeeSerializer, ProjectSerializer, TaskSerializer


class DepartmentAPIView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, pk):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        department = self.get_object(pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND


class EmployeeAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            employee = self.get_object(pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)

        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND


class ProjectAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            project = self.get_object(pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)

        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND


class TaskAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            task = self.get_object(pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)

        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

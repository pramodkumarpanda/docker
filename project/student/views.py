from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics,request
from .models import Students
from .serializers import StudentsSerializer

def index(request):
	return HttpResponse("Hi Welcome to home page")

class ListStudentsView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = Students.objects.all()
	serializer_class = StudentsSerializer

class DetailStudentView(generics.RetrieveAPIView):
	print(id)
	queryset = Students.objects.filter()
	serializer_class = StudentsSerializer
class StudentCreateApiView(generics.CreateAPIView):
	queryset=Students.objects.create()
	serializer_class = StudentsSerializer
class StudentDeleteApiView(generics.DestroyAPIView):
	queryset=Students.objects.filter().delete()
	serializer_class = StudentsSerializer

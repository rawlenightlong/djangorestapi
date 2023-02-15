from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializer

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    # The main Query for the index route:
    queryset = Todo.objects.all()
    
    # The serializer class for serializing output
    # Serializers take one thing and turn them into another thing 
    serializer_class = TodoSerializer
    
    # optional permission class to set permission level:
    permission_class = [permissions.AllowAny]
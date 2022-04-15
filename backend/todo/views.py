from django.shortcuts import render
# import view sets from the REST framework
from rest_framework import viewsets 
# import the TodoSerializer from the serializer file
from .serializers import TodoSerializer 
# import the Todo model from the models file
from .models import AdInfo

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = AdInfo.objects.all()

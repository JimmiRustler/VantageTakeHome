from django.shortcuts import render
from rest_framework import viewsets
from .serializer import adSerializer
from .models import ad

# Create your views here.

class adView(viewsets.ModelViewSet):
    serializer_class = adSerializer
    queryset = ad.objects.all()
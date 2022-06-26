
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import AirlineSerializer

from .models import Airline

# Create your views here.


class AirlineList(viewsets.ModelViewSet):
    model = Airline
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

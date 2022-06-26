
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import FlightSerializer

from .models import Flight

# Create your views here.



class FlightList(viewsets.ModelViewSet):
    model = Flight
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightDetailView(DetailView):
    model = Flight


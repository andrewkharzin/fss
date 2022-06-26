
from django.shortcuts import render, get_object_or_404, redirect
import django_tables2 as tables
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from apps.scheduler import serializers
from django_tables2 import SingleTableView
from apps.flight.models import Flight

from .models import Plan
from .tables import PlanTable


from apps.scheduler.serializers import PlanSerializer
from .models import Plan

# Create your views here.


class PlanList(viewsets.ModelViewSet):
    model = Plan
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer




class PlanListView(SingleTableView):
    model = Plan
    table_class = PlanTable
    template_name = 'plan_boards.html'
    # task_approved = tables.Column(attrs={"td": {"bgcolor": "black"}})

    


def plan_table(request):
    plans = Plan.objects.all()
    context = {
        "plans": plans
    }
    return render(request, 'plan_boards.html', context)

def flight_detail(request, pk):
  return render(request, 'plans/flight_detail.html', {
    'flight': get_object_or_404(Flight, pk=id)
  })
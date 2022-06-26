from django.shortcuts import render, get_object_or_404
from apps.scheduler.models import Plan
from django.views.generic import ListView


def home(request):
    return render(request, "home.html", {})


def plan_board(request):
    return render(request, "plan_boards.html", {})


# def flights(request):
#     return render(request, 'plan_boards.html', {'flights': Plan.objects.all()})

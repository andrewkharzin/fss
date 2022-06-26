from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.PlanList),
    path('fpboard/', PlanListView.as_view()),
]

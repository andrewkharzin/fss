from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlightList),
    path('flight/<id:pk>/', FlightDetailView.as_view(), name='flight-detail'),
]

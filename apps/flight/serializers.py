from rest_framework import routers, serializers, viewsets
from .models import Flight


class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = [
            'id',
            'flight_kind',
            'flight_date',
            'flight_co',
            'flight_number',
            'flight_ac_type',
            'flight_ac_reg_number',
        ]

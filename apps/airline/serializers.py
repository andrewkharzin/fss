from rest_framework import routers, serializers, viewsets
from .models import Airline


class AirlineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Airline
        fields = [
            'airline_shortname',
            'airline_name',
        ]

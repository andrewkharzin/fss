from import_export import resources
from .models import Airline

class PersonResource(resources.ModelResource):
    class Meta:
        model = Airline
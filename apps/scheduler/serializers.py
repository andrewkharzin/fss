from rest_framework import routers, serializers, viewsets
from .models import Plan


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = [
            'task_type',
            'get_task_date',
            'task_flight',
            'task_info',
            'task_status',
            'task_approved',
            'task_completed',
            'task_addtime',
            'task_updatetime',
        ]

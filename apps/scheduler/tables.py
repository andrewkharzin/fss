import django_tables2 as tables
from .models import Plan


class PlanTable(tables.Table):
    # task_completed = tables.Column(attrs={"td": {"id": "input-16"}})
    # task_flight = tables.LinkColumn(text='static text', args=[('pk')])

    class Meta:

        model = Plan
        template_name = "django_tables2/bootstrap.html"
        fields = (
            'task_type',
            'task_date',
            'task_flight',
            'task_status',
            'task_approved',
            'task_completed',
            'task_info',
        )
        # row_attrs = {
        #     "style": lambda record: "background-color: #8B0000;" if record['Warning'] else "background-color: #000000;"}

        attrs = {'table': 'table table-striped table-hover'}

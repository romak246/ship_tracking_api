import django_filters
from tracking.models.event import Event


class EventFilter(django_filters.FilterSet):
    event_type = django_filters.BaseCSVFilter(field_name='event_type', lookup_expr='in')

    class Meta:
        model = Event
        fields = ['event_type']

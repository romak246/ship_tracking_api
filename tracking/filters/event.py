import django_filters
from tracking.models.event import Event


class EventFilter(django_filters.FilterSet):
    event_type = django_filters.CharFilter(field_name='event_type')

    class Meta:
        model = Event
        fields = ['event_type']

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters

from tracking.filters.event import EventFilter
from tracking.models.event import Event
from tracking.serializers.event import EventSerializer


class EventViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
        Возвращает список событий
        ---
        * **search** - поиск событий по коду судна
        * **ordering** - сортировка по дате
        * **event_type** - фильтрация по типу
    """
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['ship__code']
    ordering_fields = ['date']
    filterset_class = EventFilter



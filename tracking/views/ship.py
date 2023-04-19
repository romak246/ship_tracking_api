from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters

from tracking.filters.ship import ShipFilter
from tracking.models.ship import Ship
from tracking.serializers.ship import ShipSerializer


class ShipViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
        Возвращает список судов
        ---
        * **search** - поиск по позывному
        * **type** - фильтр по типу судна
    """
    model = Ship
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer
    lookup_field = 'code'
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ShipFilter
    search_fields = ['codename']

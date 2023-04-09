from rest_framework import mixins, viewsets, filters

from tracking.models.ship import Ship
from tracking.serializers.ship import ShipSerializer


class ShipViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
        Возвращает список судов
        ---
        * **search** - поиск по коду судна
    """
    model = Ship
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer
    lookup_field = 'code'
    filter_backends = [filters.SearchFilter]
    search_fields = ['code']

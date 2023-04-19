from rest_framework import mixins, viewsets, filters

from tracking.models.port import Port
from tracking.serializers.port import PortSerializer


class PortViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
        Возвращает список портов
        ---
        * **search** - поиск порта по коду
    """
    model = Port
    queryset = Port.objects.all()
    serializer_class = PortSerializer
    lookup_field = 'code'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['code']

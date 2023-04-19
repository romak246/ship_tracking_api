import django_filters

from tracking.models.ship import Ship


class ShipFilter(django_filters.FilterSet):
    type = django_filters.BaseCSVFilter(field_name='type', lookup_expr='in')

    class Meta:
        model = Ship
        fields = ['type']

import django_filters

from tracking.models.ship import Ship


class ShipFilter(django_filters.FilterSet):
    type = django_filters.CharFilter(field_name='type')

    class Meta:
        model = Ship
        fields = ['type']

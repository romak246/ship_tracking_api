from rest_framework import serializers

from tracking.models.event import Event
from tracking.serializers.ship import ShipSerializer


class EventSerializer(serializers.ModelSerializer):
    ship = ShipSerializer()

    class Meta:
        model = Event
        fields = ['id', 'event_type', 'ship', 'date', 'latitude', 'longitude']

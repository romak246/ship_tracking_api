from rest_framework import serializers

from tracking.models.event import Event
from tracking.serializers.ship import ShipSerializer


class EventSerializer(serializers.ModelSerializer):
    ship = ShipSerializer()
    event_type = serializers.SerializerMethodField()

    @staticmethod
    def get_event_type(obj):
        return obj.get_event_type_display()

    class Meta:
        model = Event
        fields = ['id', 'event_type', 'ship', 'date', 'latitude', 'longitude']

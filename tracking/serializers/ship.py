from rest_framework import serializers

from tracking.models.ship import Ship


class ShipSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    @staticmethod
    def get_country(obj):
        return obj.country.name

    @staticmethod
    def get_type(obj):
        return obj.get_type_display()

    class Meta:
        model = Ship
        fields = ['id', 'country', 'code', 'tonnage', 'type', 'latitude', 'longitude']

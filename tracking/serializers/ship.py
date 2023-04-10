from rest_framework import serializers

from tracking.models.ship import Ship

FLAGS_STATIC_DIR = '/static/flags/'


class ShipSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    flag = serializers.SerializerMethodField()

    @staticmethod
    def get_country(obj):
        return obj.country.name

    @staticmethod
    def get_flag(obj):
        return f"{FLAGS_STATIC_DIR}{obj.country.code.lower()}.gif"

    @staticmethod
    def get_type(obj):
        return obj.get_type_display()

    class Meta:
        model = Ship
        fields = ['id', 'country', 'flag', 'code', 'tonnage', 'type', 'latitude', 'longitude']

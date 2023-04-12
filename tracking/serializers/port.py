from rest_framework import serializers

from tracking.models.port import Port

FLAGS_STATIC_DIR = '/static/flags/'


class PortSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    flag = serializers.SerializerMethodField()

    @staticmethod
    def get_country(obj):
        return obj.country.name

    @staticmethod
    def get_flag(obj):
        return f"{FLAGS_STATIC_DIR}{obj.country.code.lower()}.gif"

    class Meta:
        model = Port
        fields = ['name', 'code', 'latitude', 'longitude', 'country', 'flag']

from django.contrib import admin

from tracking.models.event import Event
from tracking.models.port import Port
from tracking.models.ship import Ship

admin.site.register(Event, )
admin.site.register(Ship, )
admin.site.register(Port, )

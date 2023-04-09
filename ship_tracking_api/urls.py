from django.contrib import admin
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from tracking.views.ship import ShipViewSet
from tracking.views.event import EventViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Ship tracking API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'ships', ShipViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('ships/', ShipViewSet.as_view(({'get': 'list'})), name='ships'),
    path('events/', EventViewSet.as_view(({'get': 'list'})), name='events')
]

from django.contrib.gis import admin
from .models import WorldBorder, Co_School, State_Bound
from leaflet.admin import LeafletGeoAdmin

admin.site.register(State_Bound, LeafletGeoAdmin)
admin.site.register(Co_School, LeafletGeoAdmin)
admin.site.register(WorldBorder, LeafletGeoAdmin)
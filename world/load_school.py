import os
from django.contrib.gis.utils import LayerMapping
from .models import Co_School

School_mapping = {
    'name' : 'Name',
    'address' : 'PropertyAd',
    'city' : 'PropertyCi',
    'jurisdiction' : 'Jurisdicti',
    'type' : 'Facility_T',
    'point' : 'POINT',

}

school_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Schools.shp'),
)



def run(verbose=True):
    lm = LayerMapping(Co_School, school_shp, School_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

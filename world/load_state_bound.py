import os
from django.contrib.gis.utils import LayerMapping
from .models import State_Bound, Co_School

state_mapping = {
    'abbrev' : 'STUSPS',
    'name' : 'NAME',
    'aland' : 'ALAND',
    'awater':'AWATER',
    'mpoly' : 'MULTIPOLYGON',
}

states_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'States.shp'),
)

def run(verbose=True):
    lm = LayerMapping(State_Bound, states_shp, state_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

School_mapping = {
    'name': 'Name',
    'address': 'PropertyAd',
    'city': 'PropertyCi',
    'jurisdiction': 'Jurisdicti',
    'type': 'Facility_T',
    'point': 'POINT',

}

school_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Schools.shp'),
)

def run(verbose=True):
    lms = LayerMapping(Co_School, school_shp, School_mapping, transform=False)
    lms.save(strict=True, verbose=verbose)

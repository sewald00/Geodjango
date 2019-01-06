from django.contrib.gis.db import models
from djgeojson.fields import PointField


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class Co_School(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    jurisdiction=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

    point=models.PointField()


    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class State_Bound(models.Model):
    abbrev= models.CharField (max_length=2)
    name=models.CharField(max_length=70)
    aland=models.IntegerField(max_length=50)
    awater=models.IntegerField(max_length=50)

    mpoly=models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


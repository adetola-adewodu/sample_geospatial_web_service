
from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)


class State(models.Model):
    ogc_fid = models.IntegerField(primary_key=True)
    wkb_geometry = models.GeometryField()
    geo_id = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    lsad = models.CharField(max_length=200)
    censusarea = models.DecimalField(max_digits=9, decimal_places=2)

class Nhdarea(models.Model):
    ogc_fid = models.IntegerField(primary_key=True)
    wkb_geometry = models.GeometryField()
    shape_area = models.DecimalField(max_digits=9, decimal_places=2)
    areasqkm = models.DecimalField(max_digits=9, decimal_places=2)
    elevation = models.DecimalField(max_digits=9, decimal_places=2)
    resolution = models.DecimalField(max_digits=9, decimal_places=2)
    fdate = models.DateField()
    permanent = models.CharField(db_column='permanent_', max_length=200)
    gnis_id = models.CharField(max_length=200)
    gnis_name = models.CharField(max_length=200)
    ftype = models.DecimalField(max_digits=9, decimal_places=2)
    fcode = models.DecimalField(max_digits=9, decimal_places=2)
    shape_leng = models.DecimalField(max_digits=9, decimal_places=2)





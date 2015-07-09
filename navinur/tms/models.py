from django.contrib.gis.db import models
# Create your models here.


class BaseMap(models.Model):
    name = models.CharField(max_length=50)
    geometry = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'tms_basemap'

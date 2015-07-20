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


class Ne50MOcean(models.Model):
    gid = models.AutoField(primary_key=True)
    scalerank = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    featurecla = models.CharField(max_length=32, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'ne_50m_ocean'
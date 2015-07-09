# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class ApproachAccuracyOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    posacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_accuracy_of_data_area'


class ApproachAdministrationAreaNamedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    jrsdtn = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_administration_area_named_area'


class ApproachAirportAirfieldArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catair = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_airport_airfield_area'


class ApproachAirportAirfieldPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catair = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_airport_airfield_point'


class ApproachAnchorBerthArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catach = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    radius = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_anchor_berth_area'


class ApproachAnchorBerthPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catach = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    radius = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_anchor_berth_point'


class ApproachAnchorageArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catach = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_anchorage_area'


class ApproachAnchorageAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catach = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_anchorage_area_point'


class ApproachBeaconCardinalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=11, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_beacon_cardinal_point'


class ApproachBeaconIsolatedDangerPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=11, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_beacon_isolated_danger_point'


class ApproachBeaconLateralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=25, blank=True, null=True)
    catlam = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_beacon_lateral_point'


class ApproachBeaconSafeWaterPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=25, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_beacon_safe_water_point'


class ApproachBeaconSpecialPurposeGeneralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=25, blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_beacon_special_purpose_general_point'


class ApproachBerthArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_berth_area'


class ApproachBerthLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_berth_line'


class ApproachBerthPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_berth_point'


class ApproachBridgeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbrg = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verccl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    vercop = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_bridge_area'


class ApproachBridgeLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbrg = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verccl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    vercop = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_bridge_line'


class ApproachBuildingSingleArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.CharField(max_length=12, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_building_single_area'


class ApproachBuildingSinglePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.CharField(max_length=12, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_building_single_point'


class ApproachBuiltUpArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbua = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_built_up_area'


class ApproachBuiltupAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbua = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_builtup_area_point'


class ApproachBuoyCardinalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    catcam = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_buoy_cardinal_point'


class ApproachBuoyIsolatedDangerPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_buoy_isolated_danger_point'


class ApproachBuoyLateralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    catlam = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_buoy_lateral_point'


class ApproachBuoySafeWaterPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_buoy_safe_water_point'


class ApproachBuoySpecialPurposeGeneralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_buoy_special_purpose_general_point'


class ApproachCableArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_cable_area'


class ApproachCableOverheadLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    icefac = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    vercsa = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_cable_overhead_line'


class ApproachCableSubmarineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_cable_submarine_line'


class ApproachCanalArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcan = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_canal_area'


class ApproachCanalLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcan = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_canal_line'


class ApproachCargoTranshipmentArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_cargo_transhipment_area'


class ApproachCausewayArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_causeway_area'


class ApproachCausewayLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_causeway_line'


class ApproachCautionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_caution_area'


class ApproachCautionAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_caution_area_point'


class ApproachCoastlineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcoa = models.CharField(max_length=20, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_coastline_line'


class ApproachCompilationScaleOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cscale = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_compilation_scale_of_data_area'


class ApproachContiguousZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_contiguous_zone_area'


class ApproachControlPointPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catctr = models.CharField(max_length=35, blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_control_point_point'


class ApproachConveyorArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcon = models.CharField(max_length=15, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    lifcap = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_conveyor_area'


class ApproachConveyorLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcon = models.CharField(max_length=15, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    lifcap = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_conveyor_line'


class ApproachCoverageArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcov = models.CharField(max_length=30, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_coverage_area'


class ApproachCraneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcrn = models.CharField(max_length=25, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    lifcap = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    radius = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_crane_area'


class ApproachCranePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcrn = models.CharField(max_length=25, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    lifcap = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    radius = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_crane_point'


class ApproachCurrentNonGravitationalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    curvel = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_current_non_gravitational_point'


class ApproachDamArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdam = models.CharField(max_length=15, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_dam_area'


class ApproachDamLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdam = models.CharField(max_length=15, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_dam_line'


class ApproachDamPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdam = models.CharField(max_length=15, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_dam_point'


class ApproachDaymarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_daymark_point'


class ApproachDeepWaterRoutePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_deep_water_route_part_area'


class ApproachDepthArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_depth_area'


class ApproachDepthAreaLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_depth_area_line'


class ApproachDepthContourLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    valdco = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_depth_contour_line'


class ApproachDistanceMarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdis = models.CharField(max_length=40, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_distance_mark_point'


class ApproachDockArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdoc = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_dock_area'


class ApproachDredgedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_dredged_area'


class ApproachDryDockArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_dry_dock_area'


class ApproachDumpingGroundArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdpg = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_dumping_ground_area'


class ApproachDumpingGroundPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdpg = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_dumping_ground_point'


class ApproachDykeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_dyke_area'


class ApproachDykeLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_dyke_line'


class ApproachExclusiveEconomicZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_exclusive_economic_zone_area'


class ApproachFairwayArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_fairway_area'


class ApproachFenceWallLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfnc = models.CharField(max_length=11, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_fence_wall_line'


class ApproachFerryRouteArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfry = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_ferry_route_area'


class ApproachFerryRouteLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfry = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_ferry_route_line'


class ApproachFishingFacilityArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfif = models.CharField(max_length=40, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_fishing_facility_area'


class ApproachFishingFacilityLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfif = models.CharField(max_length=15, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_fishing_facility_line'


class ApproachFishingFacilityPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfif = models.CharField(max_length=15, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_fishing_facility_point'


class ApproachFishingGroundArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_fishing_ground_area'


class ApproachFloatingDockArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    lifcap = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_floating_dock_area'


class ApproachFloatingDockLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    lifcap = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_floating_dock_line'


class ApproachFogSignalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfog = models.CharField(max_length=20, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    sigfrq = models.FloatField(blank=True, null=True)
    siggen = models.FloatField(blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigper = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_fog_signal_point'


class ApproachFortifiedStructureArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfor = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_fortified_structure_area'


class ApproachFortifiedStructurePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfor = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_fortified_structure_point'


class ApproachGateArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catgat = models.CharField(max_length=40, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_gate_area'


class ApproachGateLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catgat = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_gate_line'


class ApproachGatePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catgat = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_gate_point'


class ApproachGridironArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_gridiron_area'


class ApproachHarbourAreaAdministrativeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_harbour_area_administrative_area'


class ApproachHarbourFacilityArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cathaf = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_harbour_facility_area'


class ApproachHarbourFacilityPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cathaf = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_harbour_facility_point'


class ApproachHulkArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cathlk = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_hulk_area'


class ApproachHulkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cathlk = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_hulk_point'


class ApproachIceArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catice = models.CharField(max_length=11, blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_ice_area'


class ApproachInshoreTrafficZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=40, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_inshore_traffic_zone_area'


class ApproachLakeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_lake_area'


class ApproachLandArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_land_area'


class ApproachLandAreaLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_land_area_line'


class ApproachLandAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_land_area_point'


class ApproachLandElevationLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_land_elevation_line'


class ApproachLandElevationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_land_elevation_point'


class ApproachLandRegionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlnd = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_land_region_area'


class ApproachLandRegionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlnd = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_land_region_point'


class ApproachLandmarkArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlmk = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_landmark_area'


class ApproachLandmarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlmk = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_landmark_point'


class ApproachLightFloatPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_light_float_point'


class ApproachLightPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlit = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    exclit = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    litchr = models.FloatField(blank=True, null=True)
    litvis = models.CharField(max_length=254, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    mltylt = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sectr1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigper = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    valnmr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_light_point'


class ApproachLocalMagneticAnomalyArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    vallma = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_local_magnetic_anomaly_area'


class ApproachLocalMagneticAnomalyPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    vallma = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_local_magnetic_anomaly_point'


class ApproachLockBasinArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_lock_basin_area'


class ApproachLogPondArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_log_pond_area'


class ApproachLogPondPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_log_pond_point'


class ApproachMagneticVariationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    ryrmgv = models.CharField(max_length=254, blank=True, null=True)
    valacm = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    valmag = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_magnetic_variation_point'


class ApproachMarineFarmCultureArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catmfa = models.CharField(max_length=25, blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_marine_farm_culture_area'


class ApproachMarineFarmCultureLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catmfa = models.CharField(max_length=25, blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_marine_farm_culture_line'


class ApproachMarineFarmCulturePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catmfa = models.CharField(max_length=25, blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_marine_farm_culture_point'


class ApproachMilitaryPracticeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catmpa = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_military_practice_area'


class ApproachMooringWarpingFacilityArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.FloatField(blank=True, null=True)
    catmor = models.CharField(max_length=25, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_mooring_warping_facility_area'


class ApproachMooringWarpingFacilityLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.FloatField(blank=True, null=True)
    catmor = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_mooring_warping_facility_line'


class ApproachMooringWarpingFacilityPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.FloatField(blank=True, null=True)
    catmor = models.CharField(max_length=25, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_mooring_warping_facility_point'


class ApproachNauticalPublicationInformationArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    pubref = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_nautical_publication_information_area'


class ApproachNavigationLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catnav = models.CharField(max_length=20, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_navigation_line'


class ApproachNavigationalSystemOfMarksArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_navigational_system_of_marks_area'


class ApproachObstructionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_obstruction_area'


class ApproachObstructionLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_obstruction_line'


class ApproachObstructionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_obstruction_point'


class ApproachOffshorePlatformArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catofp = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_offshore_platform_area'


class ApproachOffshorePlatformPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catofp = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_offshore_platform_point'


class ApproachOffshoreProductionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpra = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_offshore_production_area'


class ApproachOilBarrierLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catolb = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_oil_barrier_line'


class ApproachPilePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catple = models.CharField(max_length=20, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_pile_point'


class ApproachPilotBoardingPlaceArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpil = models.CharField(max_length=27, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    npldst = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    pildst = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_pilot_boarding_place_area'


class ApproachPilotBoardingPlacePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpil = models.CharField(max_length=27, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    npldst = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    pildst = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_pilot_boarding_place_point'


class ApproachPipelineArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_pipeline_area'


class ApproachPipelineOverheadLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_pipeline_overhead_line'


class ApproachPipelineSubmarineOnLandLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_pipeline_submarine_on_land_line'


class ApproachPipelineSubmarineOnLandPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_pipeline_submarine_on_land_point'


class ApproachPrecautionaryArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_precautionary_area'


class ApproachProductionStorageArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpra = models.CharField(max_length=30, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_production_storage_area'


class ApproachProductionStorageAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpra = models.CharField(max_length=30, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_production_storage_area_point'


class ApproachPylonBridgeSupportArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpyl = models.CharField(max_length=60, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_pylon_bridge_support_area'


class ApproachPylonBridgeSupportPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpyl = models.CharField(max_length=60, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_pylon_bridge_support_point'


class ApproachQualityOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catqua = models.FloatField(blank=True, null=True)
    catzoc = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    posacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    surend = models.CharField(max_length=254, blank=True, null=True)
    sursta = models.CharField(max_length=254, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_quality_of_data_area'


class ApproachRadarTransponderBeaconPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrtb = models.CharField(max_length=40, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    radwal = models.CharField(max_length=254, blank=True, null=True)
    sectr1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_radar_transponder_beacon_point'


class ApproachRadioCallingInPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_radio_calling_in_point'


class ApproachRadioStationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    calsgn = models.CharField(max_length=254, blank=True, null=True)
    catros = models.CharField(max_length=254, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    estrng = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sigfrq = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_radio_station_point'


class ApproachRailwayLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_railway_line'


class ApproachRapidsArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_rapids_area'


class ApproachRapidsLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_rapids_line'


class ApproachRapidsPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_rapids_point'


class ApproachRecommendedRouteCenterlineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=50, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_recommended_route_centerline_line'


class ApproachRecommendedTrackArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=50, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_recommended_track_area'


class ApproachRecommendedTrackLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=50, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_recommended_track_line'


class ApproachRecommendedTrafficLanePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_recommended_traffic_lane_part_area'


class ApproachRescueStationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrsc = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_rescue_station_point'


class ApproachRestrictedAreaArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrea = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_restricted_area_area'


class ApproachRetroReflectorPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_retro_reflector_point'


class ApproachRiverArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_river_area'


class ApproachRiverLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_river_line'


class ApproachRoadLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrod = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_road_line'


class ApproachRunwayArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrun = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_runway_area'


class ApproachRunwayLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrun = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_runway_line'


class ApproachSandWavesArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_sand_waves_area'


class ApproachSandWavesLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_sand_waves_line'


class ApproachSandWavesPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_sand_waves_point'


class ApproachSeaAreaNamedWaterArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsea = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_sea_area_named_water_area'


class ApproachSeaAreaNamedWaterAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsea = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_sea_area_named_water_area_point'


class ApproachSeaPlaneLandingArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    valdco = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_sea_plane_landing_area'


class ApproachSeaPlaneLandingAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    valdco = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_sea_plane_landing_area_point'


class ApproachSeabedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_seabed_area'


class ApproachSeabedAreaLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_seabed_area_line'


class ApproachSeabedAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_seabed_area_point'


class ApproachShorelineConstructionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslc = models.CharField(max_length=25, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_shoreline_construction_area'


class ApproachShorelineConstructionLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslc = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_shoreline_construction_line'


class ApproachShorelineConstructionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslc = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_shoreline_construction_point'


class ApproachSignalStationTrafficPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsit = models.CharField(max_length=254, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_signal_station_traffic_point'


class ApproachSignalStationWarningPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsiw = models.CharField(max_length=254, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_signal_station_warning_point'


class ApproachSiloTankArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.FloatField(blank=True, null=True)
    catsil = models.CharField(max_length=16, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_silo_tank_area'


class ApproachSlopeToplineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslo = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_slope_topline_line'


class ApproachSlopingGroundArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslo = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_sloping_ground_area'


class ApproachSlopingGroundPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslo = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_sloping_ground_point'


class ApproachSmallCraftFacilityArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catscf = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_small_craft_facility_area'


class ApproachSmallCraftFacilityPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catscf = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_small_craft_facility_point'


class ApproachSoundingDatumArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_sounding_datum_area'


class ApproachSoundingPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    geom = models.PointField(dim=4, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_sounding_point'


class ApproachSpringPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_spring_point'


class ApproachSweptArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_swept_area'


class ApproachTidewayArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_tideway_area'


class ApproachTidewayLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_tideway_line'


class ApproachTopmarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_topmark_point'


class ApproachTrafficSeparationSchemeLanePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=11, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_traffic_separation_scheme_lane_part_area'


class ApproachTrafficSeparationZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=11, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_traffic_separation_zone_area'


class ApproachTrafficeSeparationLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=15, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_traffice_separation_line'


class ApproachTrafficeSeparationSchemaBoundaryLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=11, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_traffice_separation_schema_boundary_line'


class ApproachTunnelArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_tunnel_area'


class ApproachTunnelLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_tunnel_line'


class ApproachTunnelPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_tunnel_point'


class ApproachTwoWayRoutePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=40, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_two_way_route_part_area'


class ApproachUnderwaterAwashRockPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_underwater_awash_rock_point'


class ApproachUnsurveyedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_unsurveyed_area'


class ApproachVegetationArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catveg = models.CharField(max_length=254, blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_vegetation_area'


class ApproachVegetationLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catveg = models.CharField(max_length=254, blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_vegetation_line'


class ApproachVegetationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catveg = models.CharField(max_length=254, blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_vegetation_point'


class ApproachVerticalDatumOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_vertical_datum_of_data_area'


class ApproachWaterTurbulenceArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwat = models.CharField(max_length=11, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_water_turbulence_area'


class ApproachWaterTurbulenceLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwat = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_water_turbulence_line'


class ApproachWaterTurbulencePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwat = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_water_turbulence_point'


class ApproachWaterfallLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_waterfall_line'


class ApproachWaterfallPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_waterfall_point'


class ApproachWeedKelpArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwed = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_weed_kelp_area'


class ApproachWeedKelpPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwed = models.CharField(max_length=15, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_weed_kelp_point'


class ApproachWreckArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwrk = models.CharField(max_length=30, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_wreck_area'


class ApproachWreckPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwrk = models.CharField(max_length=30, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'approach_wreck_point'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')


    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = ['group', 'permission']


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = ['content_type', 'codename']


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = ['user', 'group']


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = ['user', 'permission']


class CoastalAccuracyOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    posacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_accuracy_of_data_area'


class CoastalAdministrationAreaNamedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    jrsdtn = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_administration_area_named_area'


class CoastalAirportAirfieldArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catair = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_airport_airfield_area'


class CoastalAirportAirfieldPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catair = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_airport_airfield_point'


class CoastalAnchorBerthPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catach = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    radius = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_anchor_berth_point'


class CoastalAnchorageArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catach = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_anchorage_area'


class CoastalAnchorageAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catach = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_anchorage_area_point'


class CoastalBeaconLateralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=25, blank=True, null=True)
    catlam = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_beacon_lateral_point'


class CoastalBeaconSafeWaterPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=25, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_beacon_safe_water_point'


class CoastalBeaconSpecialPurposeGeneralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=25, blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_beacon_special_purpose_general_point'


class CoastalBridgeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbrg = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verccl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    vercop = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_bridge_area'


class CoastalBridgeLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbrg = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verccl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    vercop = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_bridge_line'


class CoastalBridgePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbrg = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verccl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    vercop = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_bridge_point'


class CoastalBuildingSingleArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.CharField(max_length=12, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_building_single_area'


class CoastalBuildingSinglePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.CharField(max_length=12, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_building_single_point'


class CoastalBuiltUpArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbua = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_built_up_area'


class CoastalBuiltupAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbua = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_builtup_area_point'


class CoastalBuoyCardinalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    catcam = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_buoy_cardinal_point'


class CoastalBuoyIsolatedDangerPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_buoy_isolated_danger_point'


class CoastalBuoyLateralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    catlam = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_buoy_lateral_point'


class CoastalBuoySafeWaterPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_buoy_safe_water_point'


class CoastalBuoySpecialPurposeGeneralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_buoy_special_purpose_general_point'


class CoastalCableArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_cable_area'


class CoastalCableOverheadLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    icefac = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    vercsa = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_cable_overhead_line'


class CoastalCableSubmarineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_cable_submarine_line'


class CoastalCanalArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcan = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_canal_area'


class CoastalCanalLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcan = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_canal_line'


class CoastalCargoTranshipmentArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_cargo_transhipment_area'


class CoastalCautionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_caution_area'


class CoastalCautionAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_caution_area_point'


class CoastalCoastguardStationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_coastguard_station_point'


class CoastalCompilationScaleOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cscale = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_compilation_scale_of_data_area'


class CoastalContiguousZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_contiguous_zone_area'


class CoastalControlPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catctr = models.CharField(max_length=35, blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_control_point'


class CoastalCoverageArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcov = models.CharField(max_length=30, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_coverage_area'


class CoastalCurrentNonGravitationalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    curvel = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_current_non_gravitational_point'


class CoastalDaymarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_daymark_point'


class CoastalDepthArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_depth_area'


class CoastalDepthAreaLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_depth_area_line'


class CoastalDepthContourLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    valdco = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_depth_contour_line'


class CoastalDredgedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_dredged_area'


class CoastalDryDockArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_dry_dock_area'


class CoastalDumpingGroundArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdpg = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_dumping_ground_area'


class CoastalDumpingGroundPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdpg = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_dumping_ground_point'


class CoastalDykeLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_dyke_line'


class CoastalExclusiveEconomicZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_exclusive_economic_zone_area'


class CoastalFairwayArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fairway_area'


class CoastalFenceWallLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfnc = models.CharField(max_length=11, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fence_wall_line'


class CoastalFerryRouteArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfry = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_ferry_route_area'


class CoastalFerryRouteLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfry = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_ferry_route_line'


class CoastalFisheryZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    recdat = models.CharField(max_length=254, blank=True, null=True)
    recind = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fishery_zone_area'


class CoastalFishingFacilityArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfif = models.CharField(max_length=40, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fishing_facility_area'


class CoastalFishingFacilityLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfif = models.CharField(max_length=15, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fishing_facility_line'


class CoastalFishingFacilityPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfif = models.CharField(max_length=15, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fishing_facility_point'


class CoastalFishingGroundArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fishing_ground_area'


class CoastalFogSignalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfog = models.CharField(max_length=20, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    sigfrq = models.FloatField(blank=True, null=True)
    siggen = models.FloatField(blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigper = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fog_signal_point'


class CoastalFortifiedStructureArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfor = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fortified_structure_area'


class CoastalFortifiedStructurePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfor = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fortified_structure_point'


class CoastalGateLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catgat = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_gate_line'


class CoastalHarbourFacilityArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cathaf = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_harbour_facility_area'


class CoastalIceArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catice = models.CharField(max_length=11, blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_ice_area'


class CoastalIncinerationArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    lnam = models.CharField(max_length=16, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    perend = models.CharField(max_length=254, blank=True, null=True)
    persta = models.CharField(max_length=254, blank=True, null=True)
    restrn = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    recdat = models.CharField(max_length=254, blank=True, null=True)
    recind = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_incineration_area'


class CoastalIncinerationAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    lnam = models.CharField(max_length=16, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    perend = models.CharField(max_length=254, blank=True, null=True)
    persta = models.CharField(max_length=254, blank=True, null=True)
    restrn = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    recdat = models.CharField(max_length=254, blank=True, null=True)
    recind = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_incineration_area_point'


class CoastalInshoreTrafficZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=40, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_inshore_traffic_zone_area'


class CoastalLakeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_lake_area'


class CoastalLandAreaLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_land_area_line'


class CoastalLandAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_land_area_point'


class CoastalLandElevationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_land_elevation_point'


class CoastalLandRegionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlnd = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_land_region_area'


class CoastalLandRegionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlnd = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_land_region_point'


class CoastalLandmarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlmk = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_landmark_point'


class CoastalLightFloatPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_light_float_point'


class CoastalLightPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlit = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    exclit = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    litchr = models.FloatField(blank=True, null=True)
    litvis = models.CharField(max_length=254, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    mltylt = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sectr1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigper = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    valnmr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_light_point'


class CoastalLocalMagneticAnomalyArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    vallma = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_local_magnetic_anomaly_area'


class CoastalLocalMagneticAnomalyPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    vallma = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_local_magnetic_anomaly_point'


class CoastalLogPondArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_log_pond_area'


class CoastalMarineFarmCultureArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catmfa = models.CharField(max_length=25, blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_marine_farm_culture_area'


class CoastalMilitaryPracticeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catmpa = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_military_practice_area'


class CoastalMooringWarpingFacilityPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.FloatField(blank=True, null=True)
    catmor = models.CharField(max_length=25, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_mooring_warping_facility_point'


class CoastalNauticalPublicationInformationArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    pubref = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_nautical_publication_information_area'


class CoastalNavigationLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catnav = models.CharField(max_length=20, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_navigation_line'


class CoastalNavigationalSystemOfMarksArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_navigational_system_of_marks_area'


class CoastalObstructionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_obstruction_area'


class CoastalObstructionLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_obstruction_line'


class CoastalObstructionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_obstruction_point'


class CoastalOffshorePlatformArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catofp = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_offshore_platform_area'


class CoastalOffshorePlatformPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catofp = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_offshore_platform_point'


class CoastalPilePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catple = models.CharField(max_length=20, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pile_point'


class CoastalPilotBoardingPlaceArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpil = models.CharField(max_length=27, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    npldst = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    pildst = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pilot_boarding_place_area'


class CoastalPilotBoardingPlacePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpil = models.CharField(max_length=27, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    npldst = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    pildst = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pilot_boarding_place_point'


class CoastalPipelineArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pipeline_area'


class CoastalPipelineOverheadLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pipeline_overhead_line'


class CoastalPipelineSubmarineOnLandLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pipeline_submarine_on_land_line'


class CoastalPontoonLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pontoon_line'


class CoastalPrecautionaryArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_precautionary_area'


class CoastalProductionStorageArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpra = models.CharField(max_length=30, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_production_storage_area'


class CoastalProductionStorageAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpra = models.CharField(max_length=30, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_production_storage_area_point'


class CoastalPylonBridgeSupportArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpyl = models.CharField(max_length=60, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pylon_bridge_support_area'


class CoastalPylonBridgeSupportPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpyl = models.CharField(max_length=60, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pylon_bridge_support_point'


class CoastalQualityOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catqua = models.FloatField(blank=True, null=True)
    catzoc = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    posacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    surend = models.CharField(max_length=254, blank=True, null=True)
    sursta = models.CharField(max_length=254, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_quality_of_data_area'


class CoastalRadarTransponderBeaconPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrtb = models.CharField(max_length=40, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    radwal = models.CharField(max_length=254, blank=True, null=True)
    sectr1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_radar_transponder_beacon_point'


class CoastalRadioCallingInPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_radio_calling_in_point'


class CoastalRadioCallingInPointLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_radio_calling_in_point_line'


class CoastalRadioStationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    calsgn = models.CharField(max_length=254, blank=True, null=True)
    catros = models.CharField(max_length=254, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    estrng = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sigfrq = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_radio_station_point'


class CoastalRapidsArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_rapids_area'


class CoastalRecommendedRouteCenterlineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=50, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_recommended_route_centerline_line'


class CoastalRecommendedTrackLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=50, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_recommended_track_line'


class CoastalRecommendedTrafficLanePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_recommended_traffic_lane_part_area'


class CoastalRescueStationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrsc = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_rescue_station_point'


class CoastalRestrictedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrea = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_restricted_area'


class CoastalRiverArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_river_area'


class CoastalRiverLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_river_line'


class CoastalRunwayArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrun = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_runway_area'


class CoastalSandWavesPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_sand_waves_point'


class CoastalSeaAreaNamedWaterArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsea = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_sea_area_named_water_area'


class CoastalSeaAreaNamedWaterAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsea = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_sea_area_named_water_area_point'


class CoastalSeabedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_seabed_area'


class CoastalSeabedAreaLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_seabed_area_line'


class CoastalSeabedAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_seabed_area_point'


class CoastalShorelineConstructionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslc = models.CharField(max_length=25, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_shoreline_construction_area'


class CoastalShorelineConstructionLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslc = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_shoreline_construction_line'


class CoastalShorelineConstructionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslc = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_shoreline_construction_point'


class CoastalSignalStationTrafficPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsit = models.CharField(max_length=254, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_signal_station_traffic_point'


class CoastalSignalStationWarningPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsiw = models.CharField(max_length=254, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_signal_station_warning_point'


class CoastalSiloTankPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.FloatField(blank=True, null=True)
    catsil = models.CharField(max_length=16, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_silo_tank_point'


class CoastalSlopeToplineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslo = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_slope_topline_line'


class CoastalSlopingGroundPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslo = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_sloping_ground_point'


class CoastalSmallCraftFacilityPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catscf = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_small_craft_facility_point'


class CoastalSoundingDatumArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_sounding_datum_area'


class CoastalSoundingPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_sounding_point'


class CoastalSpringPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_spring_point'


class CoastalStraightTerritorialSeaBaselineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    recdat = models.CharField(max_length=254, blank=True, null=True)
    recind = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_straight_territorial_sea_baseline_line'


class CoastalTerritorialSeaArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    restrn = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    recdat = models.CharField(max_length=254, blank=True, null=True)
    recind = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_territorial_sea_area'


class CoastalTidalStreamFloodEbbPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cat_ts = models.CharField(max_length=20, blank=True, null=True)
    curvel = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_tidal_stream_flood_ebb_point'


class CoastalTidalStreamTimeSeriesPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    timend = models.CharField(max_length=254, blank=True, null=True)
    timsta = models.CharField(max_length=254, blank=True, null=True)
    t_tint = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    ts_tsv = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    recdat = models.CharField(max_length=254, blank=True, null=True)
    recind = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_tidal_stream_time_series_point'


class CoastalTopmarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_topmark_point'


class CoastalTrafficSeparationSchemeLanePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=11, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_traffic_separation_scheme_lane_part_area'


class CoastalTrafficSeparationZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=11, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_traffic_separation_zone_area'


class CoastalTrafficeSeparationSchemaBoundaryLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=11, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_traffice_separation_schema_boundary_line'


class CoastalTwoWayRoutePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=40, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_two_way_route_part_area'


class CoastalUnderwaterAwashRockPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_underwater_awash_rock_point'


class CoastalUnsurveyedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_unsurveyed_area'


class CoastalVegetationArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catveg = models.CharField(max_length=254, blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_vegetation_area'


class CoastalVegetationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catveg = models.CharField(max_length=254, blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_vegetation_point'


class CoastalVerticalDatumOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_vertical_datum_of_data_area'


class CoastalWaterTurbulenceArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwat = models.CharField(max_length=11, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_water_turbulence_area'


class CoastalWaterTurbulenceLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwat = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_water_turbulence_line'


class CoastalWaterTurbulencePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwat = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_water_turbulence_point'


class CoastalWaterfallLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_waterfall_line'


class CoastalWaterfallPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_waterfall_point'


class CoastalWeedKelpArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwed = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_weed_kelp_area'


class CoastalWeedKelpPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwed = models.CharField(max_length=15, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_weed_kelp_point'


class CoastalWreckArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwrk = models.CharField(max_length=30, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_wreck_area'


class CoastalWreckPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwrk = models.CharField(max_length=30, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_wreck_point'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'django_site'


class GeneralAdministrationAreaNamedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    jrsdtn = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_administration_area_named_area'


class GeneralAirportAirfieldPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catair = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_airport_airfield_point'


class GeneralAnchorageArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catach = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_anchorage_area'


class GeneralAnchorageAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catach = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_anchorage_area_point'


class GeneralBeaconLateralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=25, blank=True, null=True)
    catlam = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_beacon_lateral_point'


class GeneralBeaconSpecialPurposeGeneralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=25, blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_beacon_special_purpose_general_point'


class GeneralBridgeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbrg = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verccl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    vercop = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_bridge_area'


class GeneralBridgeLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbrg = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verccl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    vercop = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_bridge_line'


class GeneralBuildUpArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbua = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_build_up_area'


class GeneralBuildingSingleArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.CharField(max_length=12, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_building_single_area'


class GeneralBuildingSinglePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.CharField(max_length=12, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_building_single_point'


class GeneralBuiltupAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbua = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_builtup_area_point'


class GeneralBuoyCardinalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    catcam = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_buoy_cardinal_point'


class GeneralBuoyIsolatedDangerPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_buoy_isolated_danger_point'


class GeneralBuoyLateralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    catlam = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_buoy_lateral_point'


class GeneralBuoySafeWaterPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_buoy_safe_water_point'


class GeneralBuoySpecialPurposeGeneralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_buoy_special_purpose_general_point'


class GeneralCableArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_cable_area'


class GeneralCableOverheadLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    icefac = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    vercsa = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_cable_overhead_line'


class GeneralCableSubmarineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_cable_submarine_line'


class GeneralCanalArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcan = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_canal_area'


class GeneralCanalLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcan = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_canal_line'


class GeneralCargoTranshipmentArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_cargo_transhipment_area'


class GeneralCautionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_caution_area'


class GeneralCautionAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_caution_area_point'


class GeneralCoastguardStationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_coastguard_station_point'


class GeneralCoastlineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcoa = models.CharField(max_length=20, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_coastline_line'


class GeneralCompilationScaleOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cscale = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_compilation_scale_of_data_area'


class GeneralContiguousZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_contiguous_zone_area'


class GeneralControlPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catctr = models.CharField(max_length=35, blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_control_point'


class GeneralCoverageArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcov = models.CharField(max_length=30, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_coverage_area'


class GeneralCurrentNonGravitationalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    curvel = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_current_non_gravitational_point'


class GeneralDaymarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_daymark_point'


class GeneralDepthArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_depth_area'


class GeneralDepthAreaLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_depth_area_line'


class GeneralDepthContourLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    valdco = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_depth_contour_line'


class GeneralDumpingGroundArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdpg = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_dumping_ground_area'


class GeneralDumpingGroundPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdpg = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_dumping_ground_point'


class GeneralExclusiveEconomicZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_exclusive_economic_zone_area'


class GeneralFairwayArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_fairway_area'


class GeneralFisheryZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    recdat = models.CharField(max_length=254, blank=True, null=True)
    recind = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_fishery_zone_area'


class GeneralFogSignalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfog = models.CharField(max_length=20, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    sigfrq = models.FloatField(blank=True, null=True)
    siggen = models.FloatField(blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigper = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_fog_signal_point'


class GeneralInshoreTrafficZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=40, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_inshore_traffic_zone_area'


class GeneralLakeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_lake_area'


class GeneralLandArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_land_area'


class GeneralLandAreaLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_land_area_line'


class GeneralLandAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_land_area_point'


class GeneralLandElevationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_land_elevation_point'


class GeneralLandRegionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlnd = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_land_region_area'


class GeneralLandRegionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlnd = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_land_region_point'


class GeneralLandmarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlmk = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_landmark_point'


class GeneralLightPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlit = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    exclit = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    litchr = models.FloatField(blank=True, null=True)
    litvis = models.CharField(max_length=254, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    mltylt = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sectr1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigper = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    valnmr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_light_point'


class GeneralLocalMagneticAnomalyPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    vallma = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_local_magnetic_anomaly_point'


class GeneralMarineFarmCultureArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catmfa = models.CharField(max_length=25, blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_marine_farm_culture_area'


class GeneralMilitaryPracticeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catmpa = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_military_practice_area'


class GeneralMooringWarpingFacilityPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.FloatField(blank=True, null=True)
    catmor = models.CharField(max_length=25, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_mooring_warping_facility_point'


class GeneralNauticalPublicationInformationArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    pubref = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_nautical_publication_information_area'


class GeneralNavigationLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catnav = models.CharField(max_length=20, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_navigation_line'


class GeneralNavigationalSystemOfMarksArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_navigational_system_of_marks_area'


class GeneralObstructionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_obstruction_area'


class GeneralObstructionLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_obstruction_line'


class GeneralObstructionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_obstruction_point'


class GeneralOffshorePlatformArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catofp = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_offshore_platform_area'


class GeneralOffshorePlatformPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catofp = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_offshore_platform_point'


class GeneralPilePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catple = models.CharField(max_length=20, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_pile_point'


class GeneralPilotBoardingPlaceArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpil = models.CharField(max_length=27, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    npldst = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    pildst = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_pilot_boarding_place_area'


class GeneralPilotBoardingPlacePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpil = models.CharField(max_length=27, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    npldst = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    pildst = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_pilot_boarding_place_point'


class GeneralPipelineOverheadLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_pipeline_overhead_line'


class GeneralPipelineSubmarineOnLandLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_pipeline_submarine_on_land_line'


class GeneralPipelineSubmarineOnLandPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_pipeline_submarine_on_land_point'


class GeneralPrecautionaryArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_precautionary_area'


class GeneralProductionStorageAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpra = models.CharField(max_length=30, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_production_storage_area_point'


class GeneralPylonBridgeSupportArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpyl = models.CharField(max_length=60, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_pylon_bridge_support_area'


class GeneralQualityOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catqua = models.FloatField(blank=True, null=True)
    catzoc = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    posacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    surend = models.CharField(max_length=254, blank=True, null=True)
    sursta = models.CharField(max_length=254, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_quality_of_data_area'


class GeneralRadarTransponderBeaconPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrtb = models.CharField(max_length=40, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    radwal = models.CharField(max_length=254, blank=True, null=True)
    sectr1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_radar_transponder_beacon_point'


class GeneralRadioStationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    calsgn = models.CharField(max_length=254, blank=True, null=True)
    catros = models.CharField(max_length=254, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    estrng = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sigfrq = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_radio_station_point'


class GeneralRestrictedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrea = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_restricted_area'


class GeneralRetroReflectorPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_retro_reflector_point'


class GeneralRiverArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_river_area'


class GeneralRiverLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_river_line'


class GeneralSeaAreaNamedWaterArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsea = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_sea_area_named_water_area'


class GeneralSeaAreaNamedWaterAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsea = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_sea_area_named_water_area_point'


class GeneralSeabedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_seabed_area'


class GeneralSeabedAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_seabed_area_point'


class GeneralShorelineConstructionLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslc = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_shoreline_construction_line'


class GeneralShorelineConstructionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslc = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_shoreline_construction_point'


class GeneralSiloTankPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.FloatField(blank=True, null=True)
    catsil = models.CharField(max_length=16, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_silo_tank_point'


class GeneralSlopingGroundArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslo = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_sloping_ground_area'


class GeneralSlopingGroundPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslo = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_sloping_ground_point'


class GeneralSoundingPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_sounding_point'


class GeneralSpringPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_spring_point'


class GeneralTidalStreamTimeSeriesPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    timend = models.CharField(max_length=254, blank=True, null=True)
    timsta = models.CharField(max_length=254, blank=True, null=True)
    t_tint = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    ts_tsv = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    recdat = models.CharField(max_length=254, blank=True, null=True)
    recind = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_tidal_stream_time_series_point'


class GeneralTopmarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_topmark_point'


class GeneralTrafficSeparationLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=15, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_traffic_separation_line'


class GeneralTrafficSeparationSchemeLanePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=11, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_traffic_separation_scheme_lane_part_area'


class GeneralTrafficSeparationZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=11, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_traffic_separation_zone_area'


class GeneralTrafficeSeparationSchemaBoundaryLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=11, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_traffice_separation_schema_boundary_line'


class GeneralTwoWayRoutePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=40, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_two_way_route_part_area'


class GeneralUnderwaterAwashRockPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_underwater_awash_rock_point'


class GeneralUnsurveyedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_unsurveyed_area'


class GeneralWaterTurbulenceLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwat = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_water_turbulence_line'


class GeneralWaterTurbulencePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwat = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_water_turbulence_point'


class GeneralWeedKelpPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwed = models.CharField(max_length=15, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_weed_kelp_point'


class GeneralWreckArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwrk = models.CharField(max_length=30, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_wreck_area'


class GeneralWreckPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwrk = models.CharField(max_length=30, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_wreck_point'


class OverviewAdministrationAreaNamedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    jrsdtn = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_administration_area_named_area'


class OverviewAnchorageAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catach = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_anchorage_area_point'


class OverviewBeaconLateralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=25, blank=True, null=True)
    catlam = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_beacon_lateral_point'


class OverviewBeaconSpecialPurposeGeneralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    bcnshp = models.CharField(max_length=25, blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_beacon_special_purpose_general_point'


class OverviewBridgeLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbrg = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verccl = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    vercop = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_bridge_line'


class OverviewBuildingSinglePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.CharField(max_length=12, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_building_single_point'


class OverviewBuiltUpArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbua = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_built_up_area'


class OverviewBuiltupAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catbua = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_builtup_area_point'


class OverviewBuoyLateralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    catlam = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_buoy_lateral_point'


class OverviewBuoySafeWaterPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_buoy_safe_water_point'


class OverviewBuoySpecialPurposeGeneralPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.CharField(max_length=11, blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_buoy_special_purpose_general_point'


class OverviewCableSubmarineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_cable_submarine_line'


class OverviewCanalLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcan = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_canal_line'


class OverviewCargoTranshipmentArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_cargo_transhipment_area'


class OverviewCautionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_caution_area'


class OverviewCautionAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_caution_area_point'


class OverviewCoastlineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcoa = models.CharField(max_length=20, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_coastline_line'


class OverviewContiguousZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_contiguous_zone_area'


class OverviewControlPointPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catctr = models.CharField(max_length=35, blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_control_point_point'


class OverviewCoverageArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcov = models.CharField(max_length=30, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_coverage_area'


class OverviewCurentNonGravitationalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    curvel = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_curent_non_gravitational_point'


class OverviewDaymarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catspm = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_daymark_point'


class OverviewDepthArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_depth_area'


class OverviewDepthAreaLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_depth_area_line'


class OverviewDepthContourLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    valdco = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_depth_contour_line'


class OverviewDumpingGroundArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdpg = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_dumping_ground_area'


class OverviewDumpingGroundPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catdpg = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_dumping_ground_point'


class OverviewExclusiveEconomicZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_exclusive_economic_zone_area'


class OverviewFogSignalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfog = models.CharField(max_length=20, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    sigfrq = models.FloatField(blank=True, null=True)
    siggen = models.FloatField(blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigper = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_fog_signal_point'


class OverviewLakeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_lake_area'


class OverviewLandArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_land_area'


class OverviewLandAreaLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_land_area_line'


class OverviewLandAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_land_area_point'


class OverviewLandElevationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_land_elevation_point'


class OverviewLandRegionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlnd = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_land_region_area'


class OverviewLandRegionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlnd = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_land_region_point'


class OverviewLandmarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlmk = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_landmark_point'


class OverviewLocalMagneticAnomalyPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    vallma = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_local_magnetic_anomaly_point'


class OverviewMilitaryPracticeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catmpa = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_military_practice_area'


class OverviewMooringWarpingFacilityPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    boyshp = models.FloatField(blank=True, null=True)
    catmor = models.CharField(max_length=25, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_mooring_warping_facility_point'


class OverviewNauticalPublicationInformationArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    pubref = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_nautical_publication_information_area'


class OverviewNavigationalSystemOfMarksArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_navigational_system_of_marks_area'


class OverviewObstructionArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_obstruction_area'


class OverviewObstructionLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_obstruction_line'


class OverviewObstructionPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catobs = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_obstruction_point'


class OverviewOffshorePlatformPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catofp = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_offshore_platform_point'


class OverviewPilePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catple = models.CharField(max_length=20, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_pile_point'


class OverviewPilotBoardingPlacePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpil = models.CharField(max_length=27, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    npldst = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    pildst = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_pilot_boarding_place_point'


class OverviewPipelineSubmarineOnLandLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_pipeline_submarine_on_land_line'


class OverviewProductionStorageAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpra = models.CharField(max_length=30, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_production_storage_area_point'


class OverviewRadarTransponderBeaconPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrtb = models.CharField(max_length=40, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    radwal = models.CharField(max_length=254, blank=True, null=True)
    sectr1 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_radar_transponder_beacon_point'


class OverviewRadioStationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    calsgn = models.CharField(max_length=254, blank=True, null=True)
    catros = models.CharField(max_length=254, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    estrng = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    sigfrq = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_radio_station_point'


class OverviewRestrictedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrea = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_restricted_area'


class OverviewRiverArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_river_area'


class OverviewRiverLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_river_line'


class OverviewSeaAreaNamedWaterArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsea = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_sea_area_named_water_area'


class OverviewSeaAreaNamedWaterAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catsea = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_sea_area_named_water_area_point'


class OverviewSeabedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_seabed_area'


class OverviewSeabedAreaPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_seabed_area_point'


class OverviewShorelineConstructionLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslc = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horclr = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    horwid = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_shoreline_construction_line'


class OverviewSiloTankPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.FloatField(blank=True, null=True)
    catsil = models.CharField(max_length=16, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_silo_tank_point'


class OverviewSlopingGroundPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catslo = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_sloping_ground_point'


class OverviewSoundingDatumArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_sounding_datum_area'


class OverviewSoundingPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_sounding_point'


class OverviewTopmarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_topmark_point'


class OverviewUnderwaterAwashRockPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_underwater_awash_rock_point'


class OverviewUnsurveyedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_unsurveyed_area'


class OverviewVerticalDatumOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_vertical_datum_of_data_area'


class OverviewWaterTurbulencePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwat = models.CharField(max_length=30, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_water_turbulence_point'


class OverviewWreckPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwrk = models.CharField(max_length=30, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    veracc = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_wreck_point'



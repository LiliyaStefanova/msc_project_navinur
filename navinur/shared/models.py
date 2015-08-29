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
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_airport_airfield_area'


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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_anchorage_area'


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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verccl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vercop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verccl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vercop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_bridge_line'


class CoastalBuildingSinglePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.CharField(max_length=12, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    icefac = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vercsa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_cable_overhead_line'


class CoastalCableSubmarineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horwid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horwid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class CoastalContiguousZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_contiguous_zone_area'


class CoastalCoverageArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcov = models.CharField(max_length=30, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_coverage_area'


class CoastalCurrentNonGravitationalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    curvel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_depth_area'


class CoastalDepthAreaLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_depth_area_line'


class CoastalDepthContourLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    valdco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_depth_contour_line'


class CoastalDredgedArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_dredged_area'


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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_exclusive_economic_zone_area'


class CoastalFairwayArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fairway_area'


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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_ferry_route_line'


class CoastalFogSignalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfog = models.CharField(max_length=20, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    sigfrq = models.FloatField(blank=True, null=True)
    siggen = models.FloatField(blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_fortified_structure_area'


class CoastalGateLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catgat = models.CharField(max_length=20, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_gate_line'


class CoastalLakeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class CoastalLightPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catlit = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    exclit = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    litchr = models.FloatField(blank=True, null=True)
    litvis = models.CharField(max_length=254, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    mltylt = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sectr1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    valnmr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class CoastalMarineFarmCultureArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catmfa = models.CharField(max_length=25, blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_nautical_publication_information_area'


class CoastalNavigationLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catnav = models.CharField(max_length=20, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_navigation_line'


class CoastalNavigationalSystemOfMarksArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class CoastalOffshorePlatformPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catofp = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pilot_boarding_place_area'


class CoastalPipelineSubmarineOnLandLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pipeline_submarine_on_land_line'


class CoastalPrecautionaryArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_precautionary_area'


class CoastalPylonBridgeSupportArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpyl = models.CharField(max_length=60, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_pylon_bridge_support_area'


class CoastalQualityOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catqua = models.FloatField(blank=True, null=True)
    catzoc = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    posacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    surend = models.CharField(max_length=254, blank=True, null=True)
    sursta = models.CharField(max_length=254, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    sectr1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class CoastalRadioStationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    calsgn = models.CharField(max_length=254, blank=True, null=True)
    catros = models.CharField(max_length=254, blank=True, null=True)
    comcha = models.CharField(max_length=254, blank=True, null=True)
    estrng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class CoastalRecommendedRouteCenterlineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=50, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_recommended_route_centerline_line'


class CoastalRecommendedTrackLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=50, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_recommended_track_line'


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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_river_line'


class CoastalSandWavesPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_sea_area_named_water_area'


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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_seabed_area'


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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horwid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horwid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horwid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class CoastalTopmarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_traffice_separation_schema_boundary_line'


class CoastalTwoWayRoutePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=40, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_unsurveyed_area'


class CoastalVegetationPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catveg = models.CharField(max_length=254, blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'coastal_water_turbulence_area'


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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class ConvertedCoastalCoverage(models.Model):
    gid = models.IntegerField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcov = models.CharField(max_length=30, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    share_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(srid=32616, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'converted_coastal_coverage'


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
    name = models.CharField(max_length=100, null=True)

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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_administration_area_named_area'


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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verccl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vercop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verccl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vercop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_build_up_area'


class GeneralBuildingSinglePoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    buishp = models.CharField(max_length=12, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class GeneralCableSubmarineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horwid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_canal_area'


class GeneralCargoTranshipmentArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class GeneralCoastlineLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcoa = models.CharField(max_length=20, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_contiguous_zone_area'


class GeneralControlPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catctr = models.CharField(max_length=35, blank=True, null=True)
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_coverage_area'


class GeneralCurrentNonGravitationalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    curvel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_depth_area'


class GeneralDepthContourLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    valdco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_exclusive_economic_zone_area'


class GeneralFairwayArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_fairway_area'


class GeneralFogSignalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catfog = models.CharField(max_length=20, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    sigfrq = models.FloatField(blank=True, null=True)
    siggen = models.FloatField(blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_inshore_traffic_zone_area'


class GeneralLakeArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    litchr = models.FloatField(blank=True, null=True)
    litvis = models.CharField(max_length=254, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    mltylt = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sectr1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    valnmr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_nautical_publication_information_area'


class GeneralNavigationalSystemOfMarksArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class GeneralOffshorePlatformPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catofp = models.CharField(max_length=254, blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class GeneralPipelineOverheadLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_pipeline_overhead_line'


class GeneralPipelineSubmarineOnLandPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class GeneralQualityOfDataArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catqua = models.FloatField(blank=True, null=True)
    catzoc = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    posacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    surend = models.CharField(max_length=254, blank=True, null=True)
    sursta = models.CharField(max_length=254, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    sectr1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    estrng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_sea_area_named_water_area'


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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horwid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_shoreline_construction_line'


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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class GeneralTopmarkPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True, null=True)
    colpat = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_traffic_separation_line'


class GeneralTrafficSeparationSchemeLanePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattss = models.CharField(max_length=11, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_traffice_separation_schema_boundary_line'


class GeneralTwoWayRoutePartArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    cattrk = models.CharField(max_length=40, blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    trafic = models.FloatField(blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'general_unsurveyed_area'


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


class GeneralWreckArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwrk = models.CharField(max_length=30, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class GridTable(models.Model):
    id = models.CharField(max_length=10, blank=True, null=True)
    gid = models.AutoField(primary_key=True)
    geom = models.PolygonField(srid=32616, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'grid_table'


class Layer(models.Model):
    topology = models.ForeignKey('Topology')
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=50)
    table_name = models.CharField(max_length=50)
    feature_column = models.CharField(max_length=50)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'layer'
        unique_together = (('topology', 'layer_id'), ('schema_name', 'table_name', 'feature_column'),)


class Ne50MOcean(models.Model):
    gid = models.AutoField(primary_key=True)
    scalerank = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    featurecla = models.CharField(max_length=32, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'ne_50m_ocean'


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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verccl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vercop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    burdep = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    catcbl = models.CharField(max_length=25, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horwid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    picrep = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_contiguous_zone_area'


class OverviewCoverageArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catcov = models.CharField(max_length=30, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_coverage_area'


class OverviewCurentNonGravitationalPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    curvel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_depth_area'


class OverviewDepthContourLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    valdco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_dumping_ground_area'


class OverviewExclusiveEconomicZoneArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    nation = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    sigper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    elevat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    functn = models.CharField(max_length=254, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_nautical_publication_information_area'


class OverviewNavigationalSystemOfMarksArea(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    natsur = models.CharField(max_length=254, blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    natqua = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class OverviewPipelineSubmarineOnLandLine(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    burdep = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    catpip = models.CharField(max_length=254, blank=True, null=True)
    condtn = models.FloatField(blank=True, null=True)
    drval1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drval2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    prodct = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_pipeline_submarine_on_land_line'


class OverviewRadarTransponderBeaconPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catrtb = models.CharField(max_length=40, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    radwal = models.CharField(max_length=254, blank=True, null=True)
    sectr1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sectr2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    siggrp = models.CharField(max_length=254, blank=True, null=True)
    sigseq = models.CharField(max_length=254, blank=True, null=True)
    valmxr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    estrng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    orient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horclr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    horwid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    natcon = models.CharField(max_length=254, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    watlev = models.FloatField(blank=True, null=True)
    inform = models.CharField(max_length=254, blank=True, null=True)
    scamin = models.FloatField(blank=True, null=True)
    sordat = models.CharField(max_length=254, blank=True, null=True)
    sorind = models.CharField(max_length=254, blank=True, null=True)
    dsnm = models.CharField(max_length=12, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_shoreline_construction_line'


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
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marsys = models.FloatField(blank=True, null=True)
    topshp = models.FloatField(blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'overview_unsurveyed_area'


class OverviewWreckPoint(models.Model):
    gid = models.AutoField(primary_key=True)
    objl = models.FloatField(blank=True, null=True)
    catwrk = models.CharField(max_length=30, blank=True, null=True)
    conrad = models.FloatField(blank=True, null=True)
    convis = models.FloatField(blank=True, null=True)
    expsou = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objnam = models.CharField(max_length=254, blank=True, null=True)
    quasou = models.CharField(max_length=254, blank=True, null=True)
    souacc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecsou = models.CharField(max_length=254, blank=True, null=True)
    valsou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    veracc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    verdat = models.FloatField(blank=True, null=True)
    verlen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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


class PathGrid(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(srid=32616, blank=True, null=True)
    land_flag = models.NullBooleanField()
    zero_depth_flag = models.NullBooleanField()
    part_land_flag = models.NullBooleanField()
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'path_grid'


class TestRoutes(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    start = models.CharField(max_length=150)
    end = models.CharField(max_length=150)
    distance = models.DecimalField(max_digits=1000, decimal_places=5, blank=True, null=True)
    geom = models.LineStringField(srid=32616, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'test_routes'


class TmsBasemap(models.Model):
    name = models.CharField(max_length=50)
    geometry = models.MultiPolygonField()
    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'tms_basemap'


class Topology(models.Model):
    name = models.CharField(unique=True, max_length=50)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'topology'

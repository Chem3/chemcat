# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bottlefile(models.Model):
    filepath = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    bottlefile_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bottlefile'


class Bottles(models.Model):
    product_name = models.CharField(max_length=128, blank=True, null=True)
    chemical = models.ForeignKey('Chemicals', models.DO_NOTHING)
    quality = models.CharField(max_length=32, blank=True, null=True)
    amount = models.FloatField()
    unit = models.ForeignKey('Units', models.DO_NOTHING, blank=True, null=True)
    shelf = models.ForeignKey('Shelves', models.DO_NOTHING)
    responsible_person = models.ForeignKey('Persons', models.DO_NOTHING, blank=True, null=True)
    registered_date = models.DateField()
    loaner = models.ForeignKey('Persons', models.DO_NOTHING, blank=True, null=True)
    barcode = models.CharField(unique=True, max_length=128)
    comments = models.CharField(max_length=256, blank=True, null=True)
    bottle_id = models.AutoField(primary_key=True)
    producer_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'bottles'


class Cabinets(models.Model):
    shortname = models.CharField(max_length=32)
    longname = models.CharField(max_length=128)
    room = models.CharField(max_length=64)
    comments = models.CharField(max_length=128, blank=True, null=True)
    cabinet_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cabinets'


class Chemicals(models.Model):
    iupac_name = models.CharField(max_length=128, blank=True, null=True)
    trivial_name = models.CharField(max_length=128)
    cas = models.CharField(max_length=32)
    formula = models.CharField(max_length=32, blank=True, null=True)
    property = models.ForeignKey('Properties', models.DO_NOTHING)
    chemical_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'chemicals'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Locations(models.Model):
    name = models.CharField(max_length=32)
    comments = models.CharField(max_length=132)
    room_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Owners(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    phone = models.IntegerField()
    email = models.CharField(max_length=64)
    owner_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'owners'


class Persons(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    person_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'persons'


class Producers(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    producer_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'producers'


class Properties(models.Model):
    property_name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=10)
    comments = models.CharField(max_length=128)
    pictogram_path = models.CharField(max_length=256)
    property_id = models.AutoField(primary_key=True)
    cabinet = models.ForeignKey(Cabinets, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'properties'


class Shelves(models.Model):
    shortname = models.CharField(max_length=32)
    longname = models.CharField(max_length=128, blank=True, null=True)
    cabinet = models.ForeignKey(Cabinets, models.DO_NOTHING)
    comments = models.CharField(max_length=128, blank=True, null=True)
    shelf_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'shelves'


class Substancesofveryhighconcern(models.Model):
    name = models.TextField()
    description = models.TextField()
    ec = models.CharField(max_length=30)
    cas = models.CharField(max_length=32)
    reason = models.TextField()
    date = models.CharField(max_length=30, blank=True, null=True)
    decurl = models.CharField(max_length=200, blank=True, null=True)
    iuclidurl = models.CharField(max_length=200, blank=True, null=True)
    supporturl = models.CharField(max_length=200, blank=True, null=True)
    responseurl = models.CharField(max_length=200, blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'substancesofveryhighconcern'


class Units(models.Model):
    short_name = models.CharField(max_length=32)
    long_name = models.CharField(max_length=64)
    si_conversion_factor = models.FloatField()
    unit_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'units'

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Bottlefile(models.Model):
    filepath = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    bottlefile_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'bottlefile'
        
        

class Cabinets(models.Model):
    shortname = models.CharField(max_length=32)
    longname = models.CharField(max_length=128)
    room = models.CharField(max_length=64)
    comments = models.CharField(max_length=128, blank=True, null=True)
    cabinet_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.longname

    class Meta:
        db_table = 'cabinets'
        

class Locations(models.Model):
    name = models.CharField(max_length=32)
    comments = models.CharField(max_length=132)
    room_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'locations'


class Persons(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    person_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.firstname + " " + self.lastname
    
    class Meta:
        db_table = 'persons'


class Producers(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    producer_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'producers'
        

class Units(models.Model):
    short_name = models.CharField(max_length=32)
    long_name = models.CharField(max_length=64)
    si_conversion_factor = models.FloatField()
    unit_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.short_name
    
    class Meta:
        db_table = 'units'
        
        
class Properties(models.Model):
    property_name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=10)
    comments = models.CharField(max_length=128)
    pictogram_path = models.CharField(max_length=256)
    property_id = models.AutoField(primary_key=True)
    cabinet = models.ForeignKey(Cabinets, models.PROTECT)
   
    def __str__(self):
        return self.property_name
    
    class Meta:
        db_table = 'properties'


class Chemicals(models.Model):
    iupac_name = models.CharField(max_length=128, blank=True, null=True)
    trivial_name = models.CharField(max_length=128)
    cas = models.CharField(max_length=32)
    formula = models.CharField(max_length=32, blank=True, null=True)
    property = models.ForeignKey('Properties', models.PROTECT)
    chemical_id = models.AutoField(primary_key=True)
   
    def __str__(self):
        return self.trivial_name #+ " | " + self.iupac_name
    
    class Meta:
        db_table = 'chemicals'
        


class Shelves(models.Model):
    shortname = models.CharField(max_length=32)
    longname = models.CharField(max_length=128, blank=True, null=True)
    cabinet = models.ForeignKey(Cabinets, models.PROTECT)
    comments = models.CharField(max_length=128, blank=True, null=True)
    shelf_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.shortname
    
    class Meta:
        db_table = 'shelves'
        
        
class Bottles(models.Model):
    product_name = models.CharField(max_length=128, blank=True, null=True)
    chemical = models.ForeignKey('Chemicals', models.PROTECT)
    quality = models.CharField(max_length=32, blank=True, null=True)
    amount = models.FloatField()
    unit = models.ForeignKey('Units', models.PROTECT, blank=True, null=True)
    shelf = models.ForeignKey('Shelves', models.PROTECT)
    responsible_person = models.ForeignKey('Persons', models.PROTECT, blank=True, null=True, related_name='responsible_person')
    registered_date = models.DateField()
    loaner = models.ForeignKey('Persons', models.PROTECT, blank=True, null=True, related_name='loaner')
    barcode = models.CharField(unique=True, max_length=128)
    comments = models.CharField(max_length=256, blank=True, null=True)
    bottle_id = models.AutoField(primary_key=True)
    producer = models.ForeignKey('Producers', models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return self.product_name#+ " | "+self.chemical.iupac_name
    
    class Meta:
        db_table = 'bottles'
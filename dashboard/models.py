from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Location(models.Model):
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'
    def __str__(self):
        return self.name
        
class InputTable(models.Model):
    location = models.CharField(db_column='Location', max_length=200, blank=True, null=True)  # Field name made lowercase.
    theater_name = models.CharField(db_column='Theater_name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    film_name = models.CharField(db_column='Film_name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    show_time = models.CharField(db_column='Show_time', max_length=200, blank=True, null=True)  # Field name made lowercase.
    place = models.CharField(max_length=300, blank=True, null=True)
    screen = models.CharField(max_length=200, blank=True, null=True)
    t_sub = models.CharField(db_column='T_sub', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contact_no = models.CharField(db_column='Contact_no', max_length=300, blank=True, null=True)  # Field name made lowercase.
    booking = models.CharField(db_column='Booking', max_length=300, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    no_show = models.CharField(db_column='No_Show', max_length=45, blank=True, null=True)  # Field name made lowercase.
    oldtheatername = models.CharField(db_column='OldTheaterName', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'input_table'


class Edition(models.Model):
    location = models.ForeignKey(Location,models.DO_NOTHING,db_column='Location', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'edition'
    
    def __str__(self):
        return self.name
    
class Places(models.Model):
    location = models.IntegerField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'places'
    def __str__(self):
        return self.name

class Theater(models.Model):
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    contactnumber = PhoneNumberField(db_column='ContactNumber', blank=True,region="IN")  # Field name made lowercase.
    screens = models.CharField(db_column='Screen',max_length=45)  # Field name made lowercase.
    place = models.ForeignKey(Places, models.DO_NOTHING, db_column='Place', blank=True, null=True)  # Field name made lowercase.
    t_sub = models.CharField(db_column='T_sub', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority',)  # Field name made lowercase.
    booking = models.TextField(db_column='Booking', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oldtheatername = models.CharField(db_column='OldTheaterName', max_length=150, blank=True, null=True)  # Field name made lowercase.  
    class Meta:
        managed = False
        db_table = 'theaters'
    def __str__(self):
        return self.name

class Screen(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    theater = models.ForeignKey(Theater,models.CASCADE,db_column='Theater', max_length=45,related_name='thrscreen')  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=45)  # Field name made lowercase.
    screen_no = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'screen'
    
    def __str__(self):
        return self.name
    

class Spread(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    location = models.ForeignKey(Location,models.DO_NOTHING,db_column='Location',blank=True, null=True)
    edt_id = models.ForeignKey(Edition,models.DO_NOTHING,db_column='Edt_id')  # Field name made lowercase.
    theater = models.CharField(db_column='Theater', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spread = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'spread'

    def __str__(self):
        return self.theater

class Editionplaces(models.Model):
    location = models.ForeignKey(Location,models.DO_NOTHING,db_column='Location')  # Field name made lowercase.
    edition = models.ForeignKey(Edition, models.CASCADE, db_column='Edition')  # Field name made lowercase.
    place = models.ForeignKey(Places,models.CASCADE,db_column = 'Place')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True,unique=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'editionplaces'

    def __str__(self):
        return str(self.place)
    

    

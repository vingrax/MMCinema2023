from django.db import models

# Create your models here.
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

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Access(models.Model):
    privilege_id = models.IntegerField(db_column='Privilege_id', blank=True, null=True)  # Field name made lowercase.
    read_access = models.CharField(max_length=45, blank=True, null=True)
    write_access = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'access'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    id = models.BigAutoField(primary_key=True)
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


class Edition(models.Model):
    location = models.IntegerField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'edition'
    
    





class Editiontheaters(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    edition = models.ForeignKey(Edition, models.DO_NOTHING, db_column='Edition', blank=True, null=True)  # Field name made lowercase.
    theater = models.ForeignKey('Theaters', models.DO_NOTHING, db_column='Theater', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'editiontheaters'





class Location(models.Model):
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'


class LocationAccess(models.Model):
    user = models.ForeignKey('Userlogin', models.DO_NOTHING, blank=True, null=True)
    locations = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_access'





class Privilege(models.Model):
    id = models.IntegerField(primary_key=True)
    module = models.CharField(db_column='Module', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'privilege'


class Screen(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    theater = models.CharField(db_column='Theater', max_length=45)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=45)  # Field name made lowercase.
    screen_no = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'screen'


class Spread(models.Model):
    id = models.OneToOneField(Edition, models.DO_NOTHING, db_column='id', primary_key=True)
    location = models.IntegerField(blank=True, null=True)
    edt_id = models.IntegerField(db_column='Edt_id')  # Field name made lowercase.
    theater = models.CharField(db_column='Theater', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spread = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spread'


class Test(models.Model):
    test = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class Theaters(models.Model):
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=100)  # Field name made lowercase.
    screen = models.CharField(db_column='Screen', max_length=100)  # Field name made lowercase.
    place = models.ForeignKey(Places, models.DO_NOTHING, db_column='Place', blank=True, null=True)  # Field name made lowercase.
    t_sub = models.CharField(db_column='T_sub', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    booking = models.CharField(db_column='Booking', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oldtheatername = models.CharField(db_column='OldTheaterName', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'theaters'


class Userlogin(models.Model):
    user_name = models.CharField(max_length=100)
    passw = models.TextField()
    name = models.CharField(max_length=100, blank=True, null=True)
    privilege = models.CharField(db_column='Privilege', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userlogin'

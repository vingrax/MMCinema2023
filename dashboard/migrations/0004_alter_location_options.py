# Generated by Django 4.1.7 on 2023-04-29 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_dailyinputs_screen_alter_location_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'managed': True, 'permissions': [('editALP', 'Can edit location Alappuzha'), ('editCLT', 'Can edit location Calicut'), ('editCHN', 'Can edit location Cochin'), ('editKNR', 'Can edit location Kannur'), ('editQLN', 'Can edit location Kollam'), ('editKTM', 'Can edit location Kottayam'), ('editMPM', 'Can edit location Malappuram'), ('editPKD', 'Can edit location Palakkad'), ('editPTA', 'Can edit location Pathanamthitta'), ('editTCR', 'Can edit location Thrissur'), ('editTVM', 'Can edit location Trivandrum')]},
        ),
    ]

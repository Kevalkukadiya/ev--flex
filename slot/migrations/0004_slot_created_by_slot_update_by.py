# Generated by Django 4.1 on 2023-01-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slot', '0003_rename_station_id_slot_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='created_by',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='slot',
            name='update_by',
            field=models.IntegerField(default=1),
        ),
    ]

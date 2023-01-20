# Generated by Django 4.1 on 2023-01-18 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('station', '0002_rename_user_type_station_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('slot_name', models.CharField(max_length=30)),
                ('per_unit_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('current_status', models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('OCCUPIED', 'OCCUPIED')], default='AVAILABLE', max_length=20)),
                ('deleted', models.IntegerField(default=0)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.station')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

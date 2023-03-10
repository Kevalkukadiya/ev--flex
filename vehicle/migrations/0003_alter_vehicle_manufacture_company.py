# Generated by Django 4.1 on 2023-01-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_alter_vehicle_vehicle_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='manufacture_company',
            field=models.CharField(choices=[('TATA', 'TATA'), ('HYUNDAI', 'HYUNDAI'), ('MG', 'MG'), ('KIA', 'KIA'), ('BMW', 'BMW'), ('AUDI', 'AUDI'), ('JAGUAR', 'JAGUAR'), ('PORSCHE', 'PORSCHE'), ('MERCEDES-BENZ', 'MERCEDES-BENZ'), ('MINI COOPER', 'MINI COOPER'), ('HERO ELECTRIC', 'HERO ELECTRIC'), ('OLA ELECTRIC', 'OLA ELECTRIC'), ('ATHER ENERGY', 'ATHER ENERGY'), ('MAHINDRA ELECTRIC', 'MAHINDRA ELECTRIC'), ('TVS', 'TVS'), ('BAJAJ', 'BAJAJ'), ('REVOLAT', 'REVOLAT'), ('AMPERE EVS', 'AMPERE EVS'), ('OKINAWA', 'OKINAWA')], default='TATA', max_length=100),
        ),
    ]

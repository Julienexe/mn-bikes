# Generated by Django 5.1.3 on 2024-11-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0004_alter_lease_driving_license_alter_lease_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lease',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lease',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

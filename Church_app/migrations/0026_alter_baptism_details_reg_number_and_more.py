# Generated by Django 4.1.5 on 2023-08-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Church_app', '0025_remove_hall_booking_end_date_hall_booking_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baptism_details',
            name='Reg_number',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='marriage_details',
            name='Reg_number',
            field=models.CharField(max_length=150, null=True),
        ),
    ]

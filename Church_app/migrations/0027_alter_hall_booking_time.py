# Generated by Django 4.1.5 on 2023-08-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Church_app', '0026_alter_baptism_details_reg_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall_booking',
            name='time',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
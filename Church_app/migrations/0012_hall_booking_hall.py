# Generated by Django 4.1.5 on 2023-07-20 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Church_app', '0011_remove_hall_booking_hall_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall_booking',
            name='hall',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Church_app.hall'),
        ),
    ]

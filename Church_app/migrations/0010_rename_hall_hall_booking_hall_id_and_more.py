# Generated by Django 4.1.5 on 2023-07-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Church_app', '0009_donation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hall_booking',
            old_name='hall',
            new_name='hall_id',
        ),
        migrations.AlterField(
            model_name='donation',
            name='rupees',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
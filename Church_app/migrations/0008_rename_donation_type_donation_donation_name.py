# Generated by Django 4.1.5 on 2023-07-19 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Church_app', '0007_type_donation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type_donation',
            old_name='donation',
            new_name='donation_name',
        ),
    ]

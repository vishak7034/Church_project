# Generated by Django 4.1.5 on 2023-07-27 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Church_app', '0022_remove_baptism_details_family_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baptism_details',
            old_name='sacrement',
            new_name='celebrant',
        ),
        migrations.RenameField(
            model_name='confirmation_details',
            old_name='sacrement',
            new_name='celebrant',
        ),
        migrations.RenameField(
            model_name='marriage_details',
            old_name='gm_baptism_name',
            new_name='celebrant',
        ),
        migrations.RemoveField(
            model_name='marriage_details',
            name='sacrement',
        ),
    ]
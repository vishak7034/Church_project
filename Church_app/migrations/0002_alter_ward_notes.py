# Generated by Django 4.1.5 on 2023-07-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Church_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ward',
            name='notes',
            field=models.TextField(max_length=150, null=True),
        ),
    ]

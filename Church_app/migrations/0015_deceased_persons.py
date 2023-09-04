# Generated by Django 4.1.5 on 2023-07-26 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Church_app', '0014_alter_family_details_joining_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='deceased_persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('baptism_name', models.CharField(max_length=150, null=True)),
                ('relation', models.CharField(max_length=150, null=True)),
                ('birthdate', models.DateField(max_length=150, null=True)),
                ('deathdate', models.DateField(max_length=150, null=True)),
                ('placeofcymetry', models.CharField(max_length=150, null=True)),
                ('family', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Church_app.family_details')),
            ],
        ),
    ]
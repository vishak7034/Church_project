# Generated by Django 4.1.5 on 2023-07-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Church_app', '0015_deceased_persons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deceased_persons',
            name='family',
        ),
        migrations.AlterField(
            model_name='deceased_persons',
            name='relation',
            field=models.CharField(choices=[('A', 'Female_head'), ('B', 'Son'), ('C', 'Daughter'), ('D', 'Grand Son'), ('E', 'Grand Daughter')], max_length=150, null=True),
        ),
    ]
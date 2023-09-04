# Generated by Django 4.1.5 on 2023-07-19 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Church_app', '0005_hall'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=150, null=True)),
                ('start_date', models.DateField(max_length=150, null=True)),
                ('end_date', models.DateField(max_length=150, null=True)),
                ('notes', models.TextField(max_length=150, null=True)),
                ('hall', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Church_app.hall')),
            ],
        ),
    ]
# Generated by Django 4.1.5 on 2023-07-27 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Church_app', '0021_alter_baptism_details_baptism_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baptism_details',
            name='family',
        ),
        migrations.RemoveField(
            model_name='confirmation_details',
            name='family',
        ),
        migrations.AddField(
            model_name='baptism_details',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Church_app.personal_details'),
        ),
        migrations.AddField(
            model_name='confirmation_details',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Church_app.personal_details'),
        ),
        migrations.CreateModel(
            name='Marriage_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reg_number', models.IntegerField(max_length=150, null=True)),
                ('marriage_date', models.DateField(max_length=150, null=True)),
                ('partner_name', models.CharField(max_length=150, null=True)),
                ('p_baptism_name', models.CharField(max_length=150, null=True)),
                ('p_house_name', models.CharField(max_length=150, null=True)),
                ('p_diocese', models.CharField(max_length=150, null=True)),
                ('p_parish', models.CharField(max_length=150, null=True)),
                ('p_father_name', models.CharField(max_length=150, null=True)),
                ('p_mother_name', models.CharField(max_length=150, null=True)),
                ('gm_baptism_name', models.CharField(max_length=150, null=True)),
                ('p_birth_date', models.DateField(max_length=150, null=True)),
                ('p_baptism_date', models.DateField(max_length=150, null=True)),
                ('sacrement', models.CharField(max_length=150, null=True)),
                ('marriage_palce', models.CharField(max_length=150, null=True)),
                ('witness_name1', models.CharField(max_length=150, null=True)),
                ('w_baptism_name1', models.CharField(max_length=150, null=True)),
                ('w_diocese1', models.CharField(max_length=150, null=True)),
                ('w_parish1', models.CharField(max_length=150, null=True)),
                ('w_house_name1', models.CharField(max_length=150, null=True)),
                ('w_father_name1', models.CharField(max_length=150, null=True)),
                ('witness_name2', models.CharField(max_length=150, null=True)),
                ('w_baptism_name2', models.CharField(max_length=150, null=True)),
                ('w_diocese2', models.CharField(max_length=150, null=True)),
                ('w_parish2', models.CharField(max_length=150, null=True)),
                ('w_house_name2', models.CharField(max_length=150, null=True)),
                ('w_father_name2', models.CharField(max_length=150, null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Church_app.personal_details')),
            ],
        ),
    ]
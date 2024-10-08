# Generated by Django 5.0.2 on 2024-03-23 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultanttype',
            name='name',
            field=models.CharField(choices=[('RADIOLOGY', 'Radiologist'), ('ONCOLOGY', 'Oncologist')], max_length=20, unique=True, verbose_name='Role Name'),
        ),
    ]

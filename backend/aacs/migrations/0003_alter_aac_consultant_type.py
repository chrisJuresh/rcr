# Generated by Django 5.0.4 on 2024-04-23 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aacs', '0002_alter_aac_consultant_type'),
        ('specialities', '0003_alter_consultanttype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aac',
            name='consultant_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specialities.consultanttype'),
        ),
    ]

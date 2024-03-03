# Generated by Django 5.0.2 on 2024-03-03 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trusts', '0001_initial'),
        ('users', '0005_rcremployeeinfo_trustemployeeinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewerinfo',
            name='trust',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trusts.trust', verbose_name='Trust'),
        ),
    ]

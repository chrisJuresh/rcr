# Generated by Django 5.0.4 on 2024-04-23 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jds', '0012_checklistanswer_rcr_comments_and_more'),
        ('specialities', '0003_alter_consultanttype_name'),
        ('trusts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AAC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField()),
                ('consultant_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specialities.consultanttype')),
                ('jds', models.ManyToManyField(to='jds.jd')),
                ('trust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trusts.trust')),
            ],
        ),
    ]

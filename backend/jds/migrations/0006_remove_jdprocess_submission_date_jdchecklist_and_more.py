# Generated by Django 5.0.3 on 2024-03-31 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jds', '0005_delete_historicaljdprocess'),
        ('specialities', '0002_alter_consultanttype_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jdprocess',
            name='submission_date',
        ),
        migrations.CreateModel(
            name='JDChecklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='checklist', to='jds.jd')),
            ],
        ),
        migrations.CreateModel(
            name='ChecklistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('required', models.BooleanField(default=False)),
                ('present', models.BooleanField(default=False)),
                ('page_numbers', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('consultant_type', models.ManyToManyField(to='specialities.consultanttype')),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='jds.jdchecklist')),
            ],
        ),
    ]
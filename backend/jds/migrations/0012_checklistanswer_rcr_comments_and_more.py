# Generated by Django 5.0.4 on 2024-04-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jds', '0011_historicaljd_diagram_jd_diagram'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistanswer',
            name='rcr_comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='checklistanswer',
            name='rsa_comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='historicaljd',
            name='status',
            field=models.CharField(default='Created', max_length=50),
        ),
        migrations.AlterField(
            model_name='jd',
            name='status',
            field=models.CharField(default='Created', max_length=50),
        ),
    ]

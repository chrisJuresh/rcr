# Generated by Django 5.0.4 on 2024-04-16 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aacs', '0001_initial'),
        ('jds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aac',
            name='jd',
            field=models.ManyToManyField(to='jds.jd'),
        ),
    ]

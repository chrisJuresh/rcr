# Generated by Django 5.0.4 on 2024-04-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aacs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aac',
            name='consultant_type',
            field=models.CharField(max_length=100),
        ),
    ]
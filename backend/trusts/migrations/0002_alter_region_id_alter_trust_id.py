# Generated by Django 5.0.1 on 2024-02-02 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trusts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trust',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-15 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_unauthenticateduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unauthenticateduser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

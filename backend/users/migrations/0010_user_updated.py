# Generated by Django 5.0.4 on 2024-04-21 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_userspecialities_consultant_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_role_remove_user_is_rcr_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='user_type',
        ),
        migrations.AddField(
            model_name='role',
            name='role',
            field=models.CharField(default='', max_length=20),
        ),
    ]
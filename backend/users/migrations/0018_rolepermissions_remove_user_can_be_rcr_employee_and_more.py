# Generated by Django 5.0.1 on 2024-02-08 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_user_can_be_rcr_employee_user_can_be_representative_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolePermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_be_reviewer', models.BooleanField(default=False)),
                ('can_be_representative', models.BooleanField(default=False)),
                ('can_be_rcr_employee', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='can_be_rcr_employee',
        ),
        migrations.RemoveField(
            model_name='user',
            name='can_be_representative',
        ),
        migrations.RemoveField(
            model_name='user',
            name='can_be_reviewer',
        ),
        migrations.AddField(
            model_name='user',
            name='perms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.rolepermissions'),
        ),
    ]
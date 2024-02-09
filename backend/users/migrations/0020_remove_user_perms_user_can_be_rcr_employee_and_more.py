# Generated by Django 5.0.1 on 2024-02-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_user_perms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='perms',
        ),
        migrations.AddField(
            model_name='user',
            name='can_be_rcr_employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='can_be_representative',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='can_be_reviewer',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='RolePermissions',
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-05 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_rename_user_type_role_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(choices=[('REVIEWER', 'Reviewer'), ('REPRESENTATIVE', 'Representative'), ('TRUST_EMPLOYEE', 'Trust Employee'), ('RCR_EMPLOYEE', 'RCR Employee'), ('', 'None')], default='', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, to='users.role'),
        ),
    ]
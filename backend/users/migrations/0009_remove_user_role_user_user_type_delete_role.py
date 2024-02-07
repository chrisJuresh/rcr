# Generated by Django 5.0.1 on 2024-02-03 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_role_role_role_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('REVIEWER', 'Reviewer'), ('REPRESENTATIVE', 'Representative'), ('TRUST_EMPLOYEE', 'Trust Employee'), ('RCR_EMPLOYEE', 'RCR Employee'), ('', 'None')], default='', max_length=20),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
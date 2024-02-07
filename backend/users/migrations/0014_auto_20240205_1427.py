from django.db import migrations

def create_roles(apps, schema_editor):
    Role = apps.get_model('users', 'Role')
    for role_name in ['REVIEWER', 'REPRESENTATIVE', 'TRUST_EMPLOYEE', 'RCR_EMPLOYEE']:
        Role.objects.get_or_create(name=role_name)

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_role_name_alter_user_roles'), 
    ]

    operations = [
        migrations.RunPython(create_roles),
    ]

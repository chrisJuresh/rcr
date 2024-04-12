# Generated by Django 5.0.4 on 2024-04-12 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jds', '0008_remove_checklist_checklist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChecklistQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('required', models.BooleanField(default=False)),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='jds.checklist')),
            ],
        ),
        migrations.CreateModel(
            name='ChecklistAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.BooleanField(default=False)),
                ('page_numbers', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField(blank=True)),
                ('jd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='jds.jd')),
                ('checklist_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='jds.checklistquestion')),
            ],
        ),
        migrations.DeleteModel(
            name='ChecklistItem',
        ),
    ]

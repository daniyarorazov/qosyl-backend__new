# Generated by Django 4.2.4 on 2023-08-21 12:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_type_project_project_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]

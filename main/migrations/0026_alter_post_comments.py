# Generated by Django 4.2.4 on 2023-08-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_project_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.JSONField(default=list),
        ),
    ]

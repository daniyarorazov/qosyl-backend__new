# Generated by Django 4.2.4 on 2023-08-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_post_comments_project_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='subscribers',
            field=models.JSONField(default=list),
        ),
    ]
# Generated by Django 4.0.4 on 2023-08-19 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_post_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contact',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='image_src',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='type_project',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

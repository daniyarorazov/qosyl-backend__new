# Generated by Django 4.2.4 on 2023-08-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_useraccount_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='subscribers',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
    ]
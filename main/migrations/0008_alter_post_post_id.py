# Generated by Django 4.0.4 on 2023-08-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_post_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(blank=True, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_post_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('project_id', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100)),
                ('work_format', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('responsibility', models.TextField()),
                ('requirements', models.TextField()),
                ('we_offer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

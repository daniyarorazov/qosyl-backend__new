# Generated by Django 4.2.4 on 2023-08-24 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_project_image_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/users/avatars/'),
        ),
    ]

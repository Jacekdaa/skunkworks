# Generated by Django 2.0 on 2018-01-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_wallpaper_logo_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallpaper',
            name='description',
            field=models.TextField(null=True),
        ),
    ]

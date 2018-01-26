# Generated by Django 2.0 on 2018-01-13 09:31

from django.db import migrations, models


def gen_uuid(apps, schema_editor):
    Wallpaper = apps.get_model('api', 'Wallpaper')
    for row in Wallpaper.objects.all():
        row.description = row.title
        row.save(update_fields=['description'])


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_wallpaper_description'),
    ]

    operations = [
        migrations.RunPython(gen_uuid),
    ]
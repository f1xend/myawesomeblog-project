# Generated by Django 3.1.2 on 2021-04-13 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='post_image',
            new_name='service_image',
        ),
    ]

# Generated by Django 3.1.2 on 2021-04-23 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_auto_20210423_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicebooking',
            name='booking_phone',
        ),
    ]

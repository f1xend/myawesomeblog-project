# Generated by Django 3.1.2 on 2021-04-20 06:04

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20210419_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, help_text='DD.MM.YYYY', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(help_text='Иван', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(help_text='Иванов', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='+79998887766', max_length=128, null=True, region=None),
        ),
    ]

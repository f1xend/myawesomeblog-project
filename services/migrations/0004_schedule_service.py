# Generated by Django 3.1.2 on 2021-04-15 05:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.service'),
            preserve_default=False,
        ),
    ]

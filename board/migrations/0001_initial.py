# Generated by Django 3.1.2 on 2021-04-08 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_name', models.CharField(max_length=30)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('waiting_status', models.BooleanField(default=True)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('comment', models.CharField(blank=True, default=None, max_length=2000)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.master')),
            ],
        ),
    ]

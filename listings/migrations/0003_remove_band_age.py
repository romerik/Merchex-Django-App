# Generated by Django 4.1.2 on 2022-10-18 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_band_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='age',
        ),
    ]
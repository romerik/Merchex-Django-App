# Generated by Django 4.1.2 on 2022-10-19 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-18 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_auto_20200818_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='total_Cost',
            new_name='total',
        ),
    ]

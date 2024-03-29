# Generated by Django 3.0.8 on 2020-07-29 09:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200729_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='valid_from',
        ),
        migrations.RemoveField(
            model_name='product',
            name='valid_to',
        ),
        migrations.AddField(
            model_name='product',
            name='exp_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='mfg_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-28 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coles', '0002_alter_coles_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coles',
            name='note',
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-05 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coles', '0008_coles_barcode_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coles',
            name='barcode_filename',
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-04 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coles', '0007_alter_coles_card_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='coles',
            name='barcode_filename',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
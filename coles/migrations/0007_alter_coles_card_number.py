# Generated by Django 4.0.4 on 2022-06-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coles', '0006_coles_last_sync_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coles',
            name='card_number',
            field=models.CharField(max_length=30),
        ),
    ]

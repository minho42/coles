# Generated by Django 4.0.4 on 2022-05-28 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coles', '0005_coles_is_last_sync_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='coles',
            name='last_sync_time',
            field=models.DateTimeField(null=True),
        ),
    ]

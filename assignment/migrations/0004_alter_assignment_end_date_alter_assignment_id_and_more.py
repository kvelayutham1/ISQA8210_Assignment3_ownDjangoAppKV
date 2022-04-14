# Generated by Django 4.0.3 on 2022-04-13 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0003_auto_20220227_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='end_date',
            field=models.DateField(default=datetime.date(9999, 12, 31)),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='start_date',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
    ]

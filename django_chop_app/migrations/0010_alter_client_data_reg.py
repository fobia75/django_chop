# Generated by Django 5.0.6 on 2024-07-09 14:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chop_app', '0009_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='data_reg',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chop_app', '0002_alter_order_connection_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='data_reg',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 3.2.9 on 2022-08-09 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_orders_received_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.FloatField(max_length=10),
        ),
    ]
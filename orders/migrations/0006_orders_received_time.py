# Generated by Django 3.2.9 on 2022-06-07 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_orders_delivered_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='received_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.9 on 2022-06-07 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_buyer_customer'),
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='seller',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.seller'),
        ),
    ]

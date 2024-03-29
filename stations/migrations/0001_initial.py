# Generated by Django 3.2.9 on 2022-06-06 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_rename_buyer_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('geolocation_latitude', models.CharField(max_length=50)),
                ('geolocation_longitude', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('phone', models.CharField(max_length=50)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.seller')),
            ],
        ),
    ]

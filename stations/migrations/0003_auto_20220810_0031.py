# Generated by Django 3.2.9 on 2022-08-10 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_alter_station_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='qunatity',
            new_name='quantity',
        ),
        migrations.CreateModel(
            name='FuelQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('time_updated', models.DateTimeField(auto_now=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.station', verbose_name='station')),
            ],
        ),
    ]
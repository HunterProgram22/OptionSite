# Generated by Django 2.1.2 on 2018-10-16 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OptionContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=10)),
                ('k_open_date', models.DateTimeField(verbose_name='Date Opened')),
                ('k_expiration_date', models.DateTimeField(verbose_name='Expiration Date')),
                ('directional_bias', models.CharField(choices=[('Bullish', 'Bullish'), ('Bearish', 'Bearish'), ('Neutral', 'Neutral')], default='Bullish', max_length=10)),
            ],
        ),
    ]

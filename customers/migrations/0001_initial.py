# Generated by Django 4.2.7 on 2023-11-29 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=10)),
                ('marital_status', models.CharField(max_length=20)),
                ('wallet_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
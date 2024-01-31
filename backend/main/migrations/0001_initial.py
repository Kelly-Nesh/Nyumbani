# Generated by Django 5.0.1 on 2024-01-31 04:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.user')),
            ],
            bases=('main.user',),
        ),
        migrations.CreateModel(
            name='Suburb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.town')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pets_allowed', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.suburb')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.agent')),
            ],
        ),
    ]
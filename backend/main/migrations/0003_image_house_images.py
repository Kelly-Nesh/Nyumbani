# Generated by Django 5.0.1 on 2024-01-31 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_house_available_house_slug_suburb_slug_town_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='house')),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='images',
            field=models.ManyToManyField(to='main.image'),
        ),
    ]
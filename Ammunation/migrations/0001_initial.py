# Generated by Django 5.0.6 on 2024-06-20 05:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomb_arma', models.CharField(max_length=100, verbose_name='Nombre')),
                ('categoria', models.CharField(max_length=50)),
                ('calibre', models.CharField(choices=[('Pistola', 'Pistola'), ('Escopeta', 'Escopeta'), ('Subfusil', 'Subfusil'), ('Fusil', 'Fusil'), ('Francotirador', 'Francotirador')], max_length=13)),
                ('precio', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999)])),
                ('stock', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('descripcion', models.TextField()),
                ('foto_arma', models.ImageField(upload_to='armas', verbose_name='Imagen')),
            ],
        ),
    ]
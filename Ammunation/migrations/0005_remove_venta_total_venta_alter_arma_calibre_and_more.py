# Generated by Django 5.0.6 on 2024-06-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ammunation', '0004_alter_arma_calibre_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='total_venta',
        ),
        migrations.AlterField(
            model_name='arma',
            name='calibre',
             field=models.CharField(choices=[('Pistola', 'Pistola'), ('Escopeta', 'Escopeta'), ('Subfusil', 'Subfusil'), ('Fusil', 'Fusil'), ('Francotirador', 'Francotirador')], max_length=13),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='ciudad',
            field=models.CharField(choices=[('Curanilahue', 'Curanilahue'), ('Concepción', 'Concepción'), ('Colina', 'Colina')], max_length=20),
        ),
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=models.CharField(choices=[('enviado', 'Enviado'), ('completado', 'Completado'), ('pendiente', 'Pendiente')], default='pendiente', max_length=10),
        ),
    ]

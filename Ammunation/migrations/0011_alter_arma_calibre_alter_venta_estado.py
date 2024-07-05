# Generated by Django 5.0.6 on 2024-07-02 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ammunation', '0010_alter_arma_calibre_alter_perfil_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arma',
            name='calibre',
             field=models.CharField(choices=[('Pistola', 'Pistola'), ('Escopeta', 'Escopeta'), ('Subfusil', 'Subfusil'), ('Fusil', 'Fusil'), ('Francotirador', 'Francotirador')], max_length=13),
        ),
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=models.CharField(choices=[('ENTREGADO', 'ENTREGADO'), ('PREPARADO', 'PREPARADO'), ('ENVIADO', 'ENVIADO'), ('EN PREPARACIÓN', 'EN PREPARACIÓN')], default='EN PREPARACIÓN', max_length=30),
        ),
    ]

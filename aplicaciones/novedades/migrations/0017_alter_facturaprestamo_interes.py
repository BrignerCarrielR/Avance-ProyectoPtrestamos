# Generated by Django 4.1.1 on 2022-10-01 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0016_alter_descuentos_empleado_alter_empresas_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaprestamo',
            name='interes',
            field=models.FloatField(default=10, null=True),
        ),
    ]

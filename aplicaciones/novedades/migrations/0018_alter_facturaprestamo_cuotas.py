# Generated by Django 4.1.1 on 2022-10-01 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0017_alter_facturaprestamo_interes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaprestamo',
            name='cuotas',
            field=models.IntegerField(default=1, null=True),
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-28 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0008_remove_facturaprestamo_capitaltotal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facturaprestamo',
            options={'ordering': ['id'], 'verbose_name': 'Prestamo', 'verbose_name_plural': 'Prestamos'},
        ),
        migrations.AddField(
            model_name='facturaprestamo',
            name='fechainicio',
            field=models.DateField(null=True),
        ),
    ]

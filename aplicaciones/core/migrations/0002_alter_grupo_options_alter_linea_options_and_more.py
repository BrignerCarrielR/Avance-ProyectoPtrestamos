# Generated by Django 4.1 on 2022-08-28 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupo',
            options={'ordering': ('id',), 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='linea',
            options={'ordering': ('id',), 'verbose_name': 'Linea', 'verbose_name_plural': 'Lineas'},
        ),
        migrations.AlterField(
            model_name='grupo',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to='core/Grupos', verbose_name='Foto'),
        ),
    ]
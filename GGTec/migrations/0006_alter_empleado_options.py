# Generated by Django 4.2.5 on 2023-10-30 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GGTec', '0005_rename_servicios_empleado_servicio_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
    ]
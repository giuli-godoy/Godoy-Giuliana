# Generated by Django 4.2.5 on 2023-10-30 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GGTec', '0002_remove_empleado_fechaservicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='servicio',
            field=models.ManyToManyField(to='GGTec.servicio', verbose_name='Servicios'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='trabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GGTec.trabajo', verbose_name='Trabajos'),
        ),
    ]

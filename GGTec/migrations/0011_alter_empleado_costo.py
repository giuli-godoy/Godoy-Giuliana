# Generated by Django 4.2.5 on 2023-11-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GGTec', '0010_alter_empleado_costo_alter_empleado_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='costo',
            field=models.PositiveSmallIntegerField(choices=[(1, '$'), (2, '$$'), (3, '$$$')], null=True),
        ),
    ]
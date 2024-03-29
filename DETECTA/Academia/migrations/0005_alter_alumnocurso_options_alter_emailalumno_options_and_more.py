# Generated by Django 4.1.7 on 2023-04-13 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academia', '0004_rename_materials_id_proveedormateriales_materiales_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumnocurso',
            options={'verbose_name': 'Matricula', 'verbose_name_plural': 'Matriculas'},
        ),
        migrations.AlterModelOptions(
            name='emailalumno',
            options={'verbose_name': 'Correo del Alumno', 'verbose_name_plural': 'Correos del Alumno'},
        ),
        migrations.AlterModelOptions(
            name='emailprofesor',
            options={'verbose_name': 'Correo del Profesor', 'verbose_name_plural': 'Correos del Profesor'},
        ),
        migrations.AlterModelOptions(
            name='emailproveedor',
            options={'verbose_name': 'Correo del Proveedor', 'verbose_name_plural': 'Correos del Proveedor'},
        ),
        migrations.AlterModelOptions(
            name='materialescurso',
            options={'verbose_name': 'Asignación de Material', 'verbose_name_plural': 'Asignación de Materiales'},
        ),
        migrations.AlterModelOptions(
            name='materialesprofesor',
            options={'verbose_name': 'Asignación de Material', 'verbose_name_plural': 'Asignación de Materiales'},
        ),
        migrations.AlterModelOptions(
            name='mediosdidacticos',
            options={'verbose_name': 'Medio Didáctico', 'verbose_name_plural': 'Medios Didácticos'},
        ),
        migrations.AlterModelOptions(
            name='mediosdidacticoscurso',
            options={'verbose_name': 'Asignación de Medio Didáctico', 'verbose_name_plural': 'Asignación de Medios Didácticos'},
        ),
        migrations.AlterModelOptions(
            name='profesorcurso',
            options={'verbose_name': 'Asignación de Curso', 'verbose_name_plural': 'Asignación de Cursos'},
        ),
        migrations.AlterModelOptions(
            name='profesormediosdidacticos',
            options={'verbose_name': 'Asignación de Medio Didáctico', 'verbose_name_plural': 'Asignación de Medios Didácticos'},
        ),
        migrations.AlterModelOptions(
            name='proveedormateriales',
            options={'verbose_name': 'Compra de Material', 'verbose_name_plural': 'Compra de Materiales'},
        ),
        migrations.AlterModelOptions(
            name='proveedormediosdidacticos',
            options={'verbose_name': 'Compra de Medio Didáctico', 'verbose_name_plural': 'Compra de Medios Didácticos'},
        ),
        migrations.AlterModelOptions(
            name='telefonoalumno',
            options={'verbose_name': 'Teléfono del Alumno', 'verbose_name_plural': 'Teléfonos del Alumno'},
        ),
        migrations.AlterModelOptions(
            name='telefonoprofesor',
            options={'verbose_name': 'Teléfono del Profesor', 'verbose_name_plural': 'Teléfonos del Profesor'},
        ),
        migrations.AlterModelOptions(
            name='telefonoproveedor',
            options={'verbose_name': 'Teléfono del Proveedor', 'verbose_name_plural': 'Teléfonos del Proveedor'},
        ),
        migrations.AddField(
            model_name='telefonoalumno',
            name='codigo_empresa',
            field=models.IntegerField(choices=[(1, 'Claro'), (2, 'Tigo'), (3, 'Movistar'), (4, 'Cootel'), (5, 'Telcel'), (6, 'Otra compañia teléfonica')], default=1, verbose_name='Compañia del Número'),
        ),
        migrations.AddField(
            model_name='telefonoalumno',
            name='codigo_tipo',
            field=models.IntegerField(choices=[(1, 'Número WhatsApp'), (2, 'Número Telegram'), (3, 'Número Móvil'), (4, 'Número Convecional')], default=1, verbose_name='Tipo de Número'),
        ),
        migrations.AddField(
            model_name='telefonoprofesor',
            name='codigo_empresa',
            field=models.IntegerField(choices=[(1, 'Claro'), (2, 'Tigo'), (3, 'Movistar'), (4, 'Cootel'), (5, 'Telcel'), (6, 'Otra compañia teléfonica')], default=1, verbose_name='Compañia del Número'),
        ),
        migrations.AddField(
            model_name='telefonoprofesor',
            name='codigo_tipo',
            field=models.IntegerField(choices=[(1, 'Número WhatsApp'), (2, 'Número Telegram'), (3, 'Número Móvil'), (4, 'Número Convecional')], default=1, verbose_name='Tipo de Número'),
        ),
        migrations.AddField(
            model_name='telefonoproveedor',
            name='codigo_empresa',
            field=models.IntegerField(choices=[(1, 'Claro'), (2, 'Tigo'), (3, 'Movistar'), (4, 'Cootel'), (5, 'Telcel'), (6, 'Otra compañia teléfonica')], default=1, verbose_name='Compañia del Número'),
        ),
        migrations.AddField(
            model_name='telefonoproveedor',
            name='codigo_tipo',
            field=models.IntegerField(choices=[(1, 'Número WhatsApp'), (2, 'Número Telegram'), (3, 'Número Móvil'), (4, 'Número Convecional')], default=1, verbose_name='Tipo de Número'),
        ),
    ]

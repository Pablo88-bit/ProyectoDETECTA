# Generated by Django 4.1.7 on 2023-05-17 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academia', '0005_alter_alumnocurso_options_alter_emailalumno_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnocurso',
            name='num_participantes_f',
        ),
        migrations.RemoveField(
            model_name='alumnocurso',
            name='num_participantes_i',
        ),
        migrations.AddField(
            model_name='cursos',
            name='num_participantes_f',
            field=models.IntegerField(null=True, verbose_name='Número final de participantes'),
        ),
        migrations.AddField(
            model_name='cursos',
            name='num_participantes_i',
            field=models.IntegerField(null=True, verbose_name='Número inicial de participantes'),
        ),
    ]

from django.db import models
import random
from datetime import datetime

# Create your models here.


#Modelo Cursos
class Cursos(models.Model):
    codigo_curso = models.CharField(max_length=11, unique=True, null=False)
    nombre_curso = models.CharField(
        max_length=80, null=False, unique=True, verbose_name='Nombre del curso')
    fecha_inicio = models.DateField(
        null=False, verbose_name='Fecha inicio') 
    fecha_final = models.DateField(
        null=False, verbose_name='Fecha final') 
    numero_horas = models.IntegerField(
        null=False, verbose_name='Número de horas duración del curso')
    observaciones_cursos = models.CharField(
        max_length=200, null=True, verbose_name='Observaciones')

    #En lugar de hacer la tabla catalogo utilice una lista que fucionará como tabla catalogo
    especialidad = [
        (1, 'Ganaderia'),
        (2, 'Agricultura'),
        (3, 'Apicultura'),
        (4, 'Avicultura'),
        (5, 'Pesca')
    ]

    codigo_especialidad = models.IntegerField(choices=especialidad, default=1) 

    def save(self, *args, **kwargs):
        if not self.id:
            self.codigo_curso = generate_codigocurso()
        super(Cursos, self).save(*args, **kwargs)

    class Meta:				        #Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'Cursos'
        verbose_name = 'Curso'	
        verbose_name_plural = 'Cursos'

    def __str__ (self):			    #Esta función nos permite retornar el objeto Cursos
    	return self.nombre_curso



#Modelo Alumnos
class Alumnos(models.Model):
    cursos = models.ManyToManyField(
         Cursos, through='AlumnoCurso')
    carnet_alumno = models.CharField(
         max_length=11, unique=True, null=False)
    nombre_alumno = models.CharField(
        max_length=80, null=False, unique=True, verbose_name='Nombre del alumno')
    username_alumno = models.CharField(
        max_length=20, null=False, unique=True, verbose_name='Nombre de usuario')
    fechanac_alumno = models.DateField(
        null=False, verbose_name='Fecha de nacimiento')
    lugar_alumno = models.CharField(
        max_length=50, null=False, verbose_name='Lugar de nacimiento')
    nacionalidad_alumno = models.CharField(
        max_length=30, null=False, verbose_name='Nacionalidad')
    observaciones_alumnos = models.CharField(max_length=200, null=True)

    # En lugar de hacer la tabla catalogo utilice una lista que fucionará como tabla catalogo
    nivel = [
        (1, 'Primaria'),
        (2, 'Secundaria'),
        (3, 'Tecnico'),
        (4, 'Universidad'),
        (5, 'Master'),
        (6, 'Doctorado')
    ]

    codigo_nivel = models.IntegerField(choices=nivel, default=1)

    def save(self, *args, **kwargs):
        if not self.id:
            self.carnet_alumno = generate_carnetalumno()
        super(Alumnos, self).save(*args, **kwargs)


    class Meta:                         #Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'Alumnos'
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'


    def __str__ (self):                    #Esta función nos permite retornar el objeto Alumnos
    	return self.nombre_alumno

#Modelo Teléfono Alumno (relación de 1 a muchos)
class TelefonoAlumno(models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete = models.CASCADE, null = True, blank = True)
    telefono_alumno = models.CharField(max_length=8, null=False, verbose_name='Teléfono')

    class Meta:                         #Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'TelefonoAlumno'
        verbose_name = 'TelefonoAlumno'


#Modelo Correo Alumno (relación de 1 a muchos)
class EmailAlumno(models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete = models.CASCADE, null = True, blank = True)
    email_alumno = models.EmailField(max_length=60, null=False, verbose_name='Correo electrónico')

    class Meta:                         #Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'EmailAlumno'
        verbose_name = 'EmailAlumno'



# Con este modelo customizado seremos capaces de establecer la relación muhos a muchos
class AlumnoCurso(models.Model):
    alumno_id = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    curso_id = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    num_participantes_i = models.IntegerField(
        null=False, verbose_name='Número inicial de participantes')
    num_participantes_f = models.IntegerField(
        null=False, verbose_name='Número final de participantes')





#Funciones genera Documents únicos(carnet, códigos, etc...)
def generate_carnetalumno():
    year = str(datetime.now().year)                         #Se obtiene el año actual
    rand_int = str(random.randint(0, 999999)).zfill(6)      #Se obtiene un número aleatorio
    my_field = f"{year}-{rand_int}ED"                       #Se guarda la nomeclatura
    return my_field                                         #Retorna el carnet
  


def generate_codigocurso():
    year = str(datetime.now().year)                         #Se obtiene el año actual
    rand_int = str(random.randint(0, 999999)).zfill(6)      #Se obtiene un número aleatorio
    my_field = f"{year}{rand_int}C-D"                       #Se guarda la nomeclatura
    return my_field                                         #Retorna el codigo


#id=1 codigo curso=20238888C-D
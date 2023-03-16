from django.db import models
import random
from datetime import datetime

# Create your models here.

# Modelo Cursos
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

    # En lugar de hacer la tabla catalogo utilice una lista que fucionará como tabla catalogo
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

    class Meta:                   # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'Cursos'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):            # Esta función nos permite retornar el objeto Cursos
        return self.nombre_curso


# Modelo Alumnos
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

    class Meta:                       # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'Alumnos'
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):                # Esta función nos permite retornar el objeto Alumnos
        return self.nombre_alumno
    
# Modelo medios didacticos
class MediosDidacticos(models.Model):
    cursos = models.ManyToManyField(Cursos, through='MediosDidacticosCurso')
    codigo_medios = models.CharField(max_length=12, unique=True, null=False)
    nombre_medio = models.CharField(max_length=80, null=False, unique=True, verbose_name='Nombre del medio did. ')
    descripcion_medio = models.CharField(max_length=200, null=True, verbose_name='Descripcion')
    cantidad = models.IntegerField(null=False, verbose_name='Cantidad')
    precio = models.IntegerField(null=False, verbose_name='Precio del producto')
    unidad_Medida = models.IntegerField(null=False, verbose_name='Unidad/medida del producto')
    fecha_caducidad = models.DateField(null=False, verbose_name='Fecha de caducidad')
    fecha_compra = models.DateField(null=False, verbose_name='Fecha de la compra del producto')
    costo_total = models.DateField(null=False, verbose_name='Costo total')
    costo_unitario = models.DateField(null=False, verbose_name='Costo Unitario')
    estado_asignacion = models.CharField(max_length=150, null=True, verbose_name='Estado de asignacion')

    def save(self, *args, **kwargs):
        if not self.id:
            self.codigo_medios = generate_codigomedios()
        super(MediosDidacticos, self).save(*args, **kwargs)

    class Meta:                  # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'Medios_didacticos'
        verbose_name = 'Medio_didactico'
        verbose_name_plural = 'Medios_didacticos'

    def __str__(self):           # Esta función nos permite retornar el objeto Medios didacticos
        return self.nombre_medio

# Modelo materiales
class Materiales(models.Model):
    cursos = models.ManyToManyField(Cursos, through='MaterialesCurso')
    codigo_material = models.CharField(max_length=12, unique=True, null=False)
    nombre_material = models.CharField(max_length=80, null=False, unique=True, verbose_name='Nombre del material ')
    descripcion_material = models.CharField(max_length=200, null=True, verbose_name='Descripcion')
    cantidadMat = models.IntegerField(null=False, verbose_name='Cantidad')
    precioMat = models.IntegerField(null=False, verbose_name='Precio del material')
    unidad_MedidaMat = models.IntegerField(null=False, verbose_name='Unidad/medida del material')
    fecha_caducidadMat = models.DateField(null=False, verbose_name='Fecha de caducidad')
    fecha_compraMat = models.DateField(null=False, verbose_name='Fecha de la compra del material')
    costo_totalMat = models.DateField(null=False, verbose_name='Costo total')
    costo_unitarioMat = models.DateField(null=False, verbose_name='Costo Unitario')

    def save(self, *args, **kwargs):
        if not self.id:
            self.codigo_material = generate_codigomaterial()
        super(Materiales, self).save(*args, **kwargs)

    class Meta:                  # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'Materiales'
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'

    def __str__(self):           # Esta función nos permite retornar el objeto Materiales
        return self.nombre_material

# Modelo Proveedor
class Proveedor(models.Model):
    materials = models.ManyToManyField(Materiales, through='ProveedorMateriales')
    mediosdidactcos = models.ManyToManyField(MediosDidacticos, through='ProveedorMediosDidacticos')
    codigo_proveedor = models.CharField(max_length=12, unique=True, null=False)
    nombre_proveedor = models.CharField(max_length=80, null=False, unique=True, verbose_name='Nombre del proveedor')
    descripcion_proveedor = models.CharField(max_length=200, null=True, verbose_name='Descripcion')
    Calidad = models.CharField(max_length=200, null=True, verbose_name='Calidad')
    direccion = models.CharField(max_length=200, null=True, verbose_name='Direccion')
    observacion = models.CharField(max_length=200, null=True, verbose_name='Observaciones')

    def save(self, *args, **kwargs):
        if not self.id:
            self.codigo_proveedor = generate_codigoproveedor()
        super(Proveedor, self).save(*args, **kwargs)

    class Meta:                  # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'Proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):           # Esta función nos permite retornar el objeto Proveedor
        return self.nombre_proveedor

# Modelo Profesor
class Profesor(models.Model):
    materiales = models.ManyToManyField(Materiales, through='MaterialesProfesor')
    mediosdidacticos = models.ManyToManyField(MediosDidacticos, through='ProfesorMediosDidacticos')
    cursos = models.ManyToManyField(Cursos, through='ProfesorCurso')
    carnet_teacher = models.CharField(max_length=11, unique=True, null=False)
    nombre_teacher = models.CharField(max_length=80, null=False, unique=True, verbose_name='Nombre del Profesor')
    fechanac_teacher = models.DateField(null=False, verbose_name='Fecha de nacimiento')
    Numero_cedula = models.DateField(null=False, verbose_name='Numero de cedula')
    lugarOrigen_teacher = models.CharField(max_length=50, null=False, verbose_name='Lugar de nacimiento')
    nacionalidad_teacher = models.CharField(max_length=60, null=False, verbose_name='Nacionalidad')
    Referencias_profecionales = models.CharField(max_length=200, null=True, verbose_name='Referencias profecionales')

    # En lugar de hacer la tabla catalogo utilice una lista que fucionará como tabla catalogo
    nivel = [
        (1, 'Tecnico'),
        (2, 'Universidad'),
        (3, 'Master'),
        (4, 'Posgrado'),
        (5, 'Doctorado')
    ]
    codigo_nivel = models.IntegerField(choices=nivel, default=1)

    genero = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('NB', 'No binario'),
        ('JUAN', 'Gay'),
        ('N', 'No especificar')
    ]
    generoTeacher = models.IntegerField(choices=genero, default=1)

    def save(self, *args, **kwargs):
        if not self.id:
            self.carnet_teacher = generate_carnetprofe()
        super(Profesor, self).save(*args, **kwargs)

    class Meta:                  # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'Profesor'
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):           # Esta función nos permite retornar el objeto Profesor
        return self.nombre_teacher

# Modelo Teléfono Alumno (relación de 1 a muchos)
class TelefonoAlumno(models.Model):
    alumno = models.ForeignKey(
        Alumnos, on_delete=models.CASCADE, null=True, blank=True)
    telefono_alumno = models.CharField(
        max_length=8, null=False, verbose_name='Teléfono')

    class Meta:                 # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'TelefonoAlumno'
        verbose_name = 'TelefonoAlumno'


# Modelo Correo Alumno (relación de 1 a muchos)
class EmailAlumno(models.Model):
    alumno = models.ForeignKey(
        Alumnos, on_delete=models.CASCADE, null=True, blank=True)
    email_alumno = models.EmailField(
        max_length=60, null=False, verbose_name='Correo electrónico')

    class Meta:                 # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'EmailAlumno'
        verbose_name = 'EmailAlumno'

# Modelo Telefono Profesor(relacion de 1 a muchos)
class TelefonoProfesor(models.Model):
    profesor = models.ForeignKey(
        Profesor, on_delete=models.CASCADE,null=True,blank=True)
    telefono_profesor=models.CharField(
      max_length=8, null=False, verbose_name='Telefono')
    
    class Meta:                  # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'TelefonoProfesor'
        verbose_name = 'TelefonoProfesor'

# Modelo Correo Profesor(relacion de 1 a muchos)
class EmailProfesor(models.Model):
    profesor = models.ForeignKey(
        Profesor, on_delete=models.CASCADE,null=True,blank=True)
    email_profesor = models.EmailField(
        max_length=70,null=False,verbose_name='Correo electronico')
    
    class Meta:                 # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'EmailProfesor'
        verbose_name = 'EmailProfesor'

# Modelo Telefono Proveedor(relacion de 1 a muchos)
class TelefonoProveedor(models.Model):
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.CASCADE, null=True,blank=True)
    telefono_proveedor=models.CharField(
        max_length=8, null=False, verbose_name='Telefono')
    
    class Meta:                  # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'TelefonoProveedor'
        verbose_name = 'TelefonoProveedor'

# Modelo Correo Proveedor(relacion de 1 a muchos)
class EmailProveedor(models.Model):
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.CASCADE,null=True,blank=True)
    email_proveedor = models.EmailField(
        max_length=70,null=False,verbose_name='Correo electronico')
    
    class Meta:                 # Clase meta podemos cambiar el nombre de tabla en la BD
        db_table = 'EmailProveedor'
        verbose_name = 'EmailProveedor'

# Con este modelo customizado seremos capaces de establecer la relación muhos a muchos
class AlumnoCurso(models.Model):
    alumno_id = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    curso_id = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    num_participantes_i = models.IntegerField(
        null=False, verbose_name='Número inicial de participantes')
    num_participantes_f = models.IntegerField(
        null=False, verbose_name='Número final de participantes')

# Modelo Cursos Profesor(relacion muchos a muchos)
class ProfesorCurso(models.Model):
    profesor_id = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    cursos_id = models.ForeignKey(Cursos, on_delete=models.CASCADE)

# Modelo cursos Medios Didacticos(Relacion muchos a muchos)
class MediosDidacticosCurso(models.Model):
    mediosdidacticos_id = models.ForeignKey(MediosDidacticos,on_delete=models.CASCADE)
    cursosid = models.ForeignKey(Cursos,on_delete=models.CASCADE)

# Modelo Cursos Materiales(relacion muchos a muchos)
class MaterialesCurso(models.Model):
    materiales_id = models.ForeignKey(Materiales,on_delete=models.CASCADE)
    cursoM_id = models.ForeignKey(Cursos, on_delete=models.CASCADE)

# Modelo Medios Didacticos Profesor(relacion muchos a muchos)
class ProfesorMediosDidacticos(models.Model):
    medios_didacticos_id =models.ForeignKey(MediosDidacticos, on_delete=models.CASCADE)
    profe_id = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    fecha_recibido = models.DateField(null=False, verbose_name='Fecha de recibido')

    # En lugar de hacer la tabla catalogo utilice una lista que fucionará como tabla catalogo
    recibido = [
        ('S', 'YES'),
        ('N', 'NO')    
    ]
    Received = models.IntegerField(choices=recibido, default=1)

# Modelo Materiales Profesor(relacion muchos a muchos)
class MaterialesProfesor(models.Model):
    materialesid = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    Profesorid=models.ForeignKey(Profesor,on_delete=models.CASCADE)
    fecha_recibdo = models.DateField(null=False, verbose_name='Fecha de recibido')

    # En lugar de hacer la tabla catalogo utilice una lista que fucionará como tabla catalogo
    recibdo = [
        ('S', 'YES'),
        ('N', 'NO')    
    ]
    Received = models.IntegerField(choices=recibdo, default=1)

# Modelo Medios Didacticos Proveedores(relacion muchos a muchos)
class ProveedorMediosDidacticos(models.Model):
    medios_didactcos_id = models.ForeignKey(MediosDidacticos, on_delete=models.CASCADE)
    proveedor_id = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    fecha_compra = models.DateField(null=False, verbose_name='Fecha de compra')
    CantidadCompra = models.IntegerField(null=False, verbose_name='Cantidad Compra')

# Modelo Materiales Proveedores(relacion muchos a muchos)
class ProveedorMateriales(models.Model):
    materials_id = models.ForeignKey(Materiales,on_delete=models.CASCADE)
    proveedorid = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    fechacompra = models.DateField(null=False, verbose_name='Fecha de compra')
    Cantidad_Compra = models.IntegerField(null=False, verbose_name='Cantidad Compra')

# Funciones genera Documents únicos(carnet, códigos, etc...)
def generate_carnetalumno():
    year = str(datetime.now().year)                     # Se obtiene el año actual
    rand_int = str(random.randint(0, 999999)).zfill(6)  # Se obtiene un número aleatorio
    my_field = f"{year}-{rand_int}ED"                   # Se guarda la nomeclatura
    return my_field                                     # Retorna el carnet

def generate_codigomedios():
    year = str(datetime.now().year)                     # Se obtiene el año actual
    rand_int = str(random.randint(0, 999999)).zfill(6)  # Se obtiene un número aleatorio
    my_field = f"{year}-{rand_int}MD"                   # Se guarda la nomeclatura
    return my_field                                     # Retorna el codigo

def generate_codigomaterial():   
    year = str(datetime.now().year)                     # Se obtiene el año actual
    rand_int = str(random.randint(0, 999999)).zfill(6)  # Se obtiene un número aleatorio
    my_field = f"{year}-{rand_int}MT"                    # Se guarda la nomeclatura
    return my_field                                     # Retorna el codigo

def generate_codigoproveedor():
    year = str(datetime.now().year)                     # Se obtiene el año actual
    rand_int = str(random.randint(0, 999999)).zfill(6)  # Se obtiene un número aleatorio
    my_field = f"{year}-{rand_int}PD"                   # Se guarda la nomeclatura
    return my_field                                     # Retorna el codigo

def generate_carnetprofe():
    year = str(datetime.now().year)                     # Se obtiene el año actual
    rand_int = str(random.randint(0, 999999)).zfill(6)  # Se obtiene un número aleatorio 
    my_field = f"{year}-{rand_int}P-D"                  # Se guarda la nomeclatura
    return my_field                                     # Retorna el codigo

def generate_codigocurso():
    year = str(datetime.now().year)                      # Se obtiene el año actual
    rand_int = str(random.randint(0, 999999)).zfill(6)   # Se obtiene un número aleatorio
    my_field = f"{year}{rand_int}C-D"                    # Se guarda la nomeclatura
    return my_field                                      # Retorna el codigo

# id=1 codigo curso=20238888C-D
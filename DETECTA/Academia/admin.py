from django.contrib import admin
from .models import Alumnos, TelefonoAlumno, EmailAlumno
from .models import Profesor, TelefonoProfesor, EmailProfesor
from .models import Proveedor, TelefonoProveedor, EmailProveedor
from .models import Cursos, Materiales, MediosDidacticos
from .models import AlumnoCurso, ProfesorCurso, MaterialesCurso, MediosDidacticosCurso
from .models import MaterialesProfesor, ProfesorMediosDidacticos
from .models import ProveedorMateriales, ProveedorMediosDidacticos

# Register your models here.
#Alumnos
admin.site.register(Alumnos)
admin.site.register(TelefonoAlumno)
admin.site.register(EmailAlumno)

#Profesores
admin.site.register(Profesor)
admin.site.register(TelefonoProfesor)
admin.site.register(EmailProfesor)

#Proveedores
admin.site.register(Proveedor)
admin.site.register(TelefonoProveedor)
admin.site.register(EmailProveedor)

#Cursos
admin.site.register(Cursos)

#Materiales y Medios Didácticos
admin.site.register(Materiales)
admin.site.register(MediosDidacticos)

#Tablas puentes
admin.site.register(AlumnoCurso)
admin.site.register(ProfesorCurso)
admin.site.register(MediosDidacticosCurso)
admin.site.register(MaterialesCurso)
admin.site.register(MaterialesProfesor)
admin.site.register(ProfesorMediosDidacticos)
admin.site.register(ProveedorMateriales)
admin.site.register(ProveedorMediosDidacticos)

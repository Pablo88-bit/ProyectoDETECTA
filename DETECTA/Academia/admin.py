from django.contrib import admin
from .models import Alumnos, TelefonoAlumno, EmailAlumno
from .models import Profesor, TelefonoProfesor, EmailProfesor
from .models import Proveedor, TelefonoProveedor, EmailProveedor
from .models import Cursos, Materiales, MediosDidacticos
from .models import AlumnoCurso, ProfesorCurso, MaterialesCurso, MediosDidacticosCurso
from .models import MaterialesProfesor, ProfesorMediosDidacticos
from .models import ProveedorMateriales, ProveedorMediosDidacticos



#class AlumnoEmailAdmin(admin.ModelAdmin):
        #=('email_alumno')
        #("telefono_alumno", "email_alumno")
class AlumnoAdmin(admin.ModelAdmin):
        list_display=('carnet_alumno', 'nombre_alumno', 'username_alumno', 'nacionalidad_alumno', 'codigo_nivel')
        search_fields=('carnet_alumno', 'nombre_alumno')
        #list_editable("telefono_alumno", "email_alumno")
        list_filter=('nacionalidad_alumno', 'lugar_alumno')




# Register your models here.
#Alumnos
admin.site.register(Alumnos, AlumnoAdmin)
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



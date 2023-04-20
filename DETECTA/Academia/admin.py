from django.contrib import admin
from django import forms
from .models import Alumnos, TelefonoAlumno, EmailAlumno
from .models import Profesor, TelefonoProfesor, EmailProfesor
from .models import Proveedor, TelefonoProveedor, EmailProveedor
from .models import Cursos, Materiales, MediosDidacticos
from .models import AlumnoCurso, ProfesorCurso, MaterialesCurso, MediosDidacticosCurso
from .models import MaterialesProfesor, ProfesorMediosDidacticos
from .models import ProveedorMateriales, ProveedorMediosDidacticos


# Register your models here.
admin.site.site_header = "ACADEMIA DETECTA"

#Vistas de Alumnos en el sistema
#######################################################################################
class AlumnoForm(forms.ModelForm):
        carnet_alumno = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 11}))

class TelefonoAlumnoInline(admin.TabularInline):
        model = TelefonoAlumno

class EmailAlumnoInline(admin.TabularInline):
        model = EmailAlumno   

#class ProfesorCursoInline(admin.TabularInline):
#        model = ProfesorCurso    

class AlumnoAdmin(admin.ModelAdmin):
        form = AlumnoForm
        list_per_page = 4
        list_display=('carnet_alumno', 'nombre_alumno', 'username_alumno', 'nacionalidad_alumno', 'codigo_nivel')
        search_fields=('carnet_alumno', 'nombre_alumno')
        #list_editable("telefono_alumno", "email_alumno")
        list_filter=('nacionalidad_alumno', 'lugar_alumno')
        inlines = [
                TelefonoAlumnoInline,
                EmailAlumnoInline,
        ] 

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False

#Alumnos
admin.site.register(Alumnos, AlumnoAdmin)











#Vistas de Profesores en el sistema
#######################################################################################

class ProfesorForm(forms.ModelForm):
        carnet_teacher = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 11}))

class TelefonoProfesorInline(admin.TabularInline):
        model = TelefonoProfesor

class EmailProfesorInline(admin.TabularInline):
        model = EmailProfesor       

class ProfesorCursoInline(admin.TabularInline):
        model = ProfesorCurso
        extra = 0
        min_num = 1

class MaterialesProfesorInline(admin.TabularInline):
        model = MaterialesProfesor
        extra = 0
        min_num = 1


class ProfesorMediosDidacticosInline(admin.TabularInline):
        model = ProfesorMediosDidacticos
        extra = 0
        min_num = 1

class   ProfesorAdmin(admin.ModelAdmin):
        form = ProfesorForm
        list_per_page = 4
        list_display=('carnet_teacher', 'nombre_teacher', 'Numero_cedula', 'sexo', 'nacionalidad_teacher', 'codigo_nivel')
        search_fields=('carnet_teacher', 'nombre_teacher')
        list_filter=('nacionalidad_teacher', 'sexo')
        inlines = [
                TelefonoProfesorInline,
                EmailProfesorInline,
                ProfesorCursoInline,
                MaterialesProfesorInline,
                ProfesorMediosDidacticosInline,
        ]

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False



#Profesores
admin.site.register(Profesor, ProfesorAdmin)











#Vistas de Proveedores en el sistema
#######################################################################################
class ProveedorForm(forms.ModelForm):
        codigo_proveedor = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 12}))

class TelefonoProveedorInline(admin.TabularInline):
        model = TelefonoProveedor

class EmailProveedorInline(admin.TabularInline):
        model = EmailProveedor       

class ProveedorMediosDidacticosInline(admin.TabularInline):
        model = ProveedorMediosDidacticos
        extra = 0
        min_num = 1

class ProveedorMaterialesInline(admin.TabularInline):
        model = ProveedorMateriales
        extra = 0
        min_num = 1

class   ProveedorAdmin(admin.ModelAdmin):
        form = ProveedorForm
        list_per_page = 4
        list_display=('codigo_proveedor', 'nombre_proveedor', 'calidad', 'direccion')
        search_fields=('codigo_proveedor', 'nombre_proveedor')
        list_filter=('nombre_proveedor', 'calidad')
        inlines = [
                TelefonoProveedorInline,
                EmailProveedorInline,
                ProveedorMediosDidacticosInline,
                ProveedorMaterialesInline,
        ]

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False

#Proveedores
admin.site.register(Proveedor, ProveedorAdmin)










#Vistas de Cursos en el sistema
#######################################################################################
class CursoForm(forms.ModelForm):
        codigo_curso = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 11}))

class MediosDidacticosCursoInline(admin.TabularInline):
        model = MediosDidacticosCurso

class MaterialesCursoInline(admin.TabularInline):
        model = MaterialesCurso


class  CursoAdmin(admin.ModelAdmin):
        form = CursoForm
        list_per_page = 4
        list_display=('codigo_curso', 'nombre_curso', 'image', 'codigo_especialidad')
        search_fields=('codigo_curso', 'nombre_curso')
        list_filter=('fecha_inicio', 'fecha_final')
        #list_filter=('calidad')
        inlines = [
                MediosDidacticosCursoInline,
                MaterialesCursoInline,
        ]

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False

#Cursos
admin.site.register(Cursos, CursoAdmin)






#Vistas de Materiales en el sistema
#######################################################################################
class MaterialesForm(forms.ModelForm):
        codigo_material = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 12}))

class MaterialesAdmin(admin.ModelAdmin):
        form = MaterialesForm
        list_per_page = 4
        list_display=('codigo_material', 'nombre_material', 'unidad_MedidaMat', 'costo_unitarioMat', 'costo_totalMat', 'cantidadMat')
        search_fields=('codigo_material', 'nombre_material')
        list_filter=('nombre_material', 'unidad_MedidaMat')

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False

#Materiales
admin.site.register(Materiales, MaterialesAdmin)








#Vistas de Medios Didácticos en el sistema
#######################################################################################
class MediosDidacticosForm(forms.ModelForm):
         codigo_medios = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 12}))


class MediosDidacticosAdmin(admin.ModelAdmin):
        form = MediosDidacticosForm
        list_per_page = 4
        list_display=('codigo_medios', 'nombre_medio', 'unidad_Medida', 'costo_unitario', 'costo_total', 'estado_asignacion')
        search_fields=('codigo_medios', 'nombre_medio')
        list_filter=('estado_asignacion', 'unidad_Medida')

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False

#Medios Didácticos
admin.site.register(MediosDidacticos, MediosDidacticosAdmin)




#Tablas puentes
#admin.site.register(AlumnoCurso)
#admin.site.register(ProfesorCurso)
#admin.site.register(MediosDidacticosCurso)
#admin.site.register(MaterialesCurso)
#admin.site.register(MaterialesProfesor)
#admin.site.register(ProfesorMediosDidacticos)
#admin.site.register(ProveedorMateriales)
#admin.site.register(ProveedorMediosDidacticos)



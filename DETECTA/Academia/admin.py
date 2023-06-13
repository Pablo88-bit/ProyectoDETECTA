from django.contrib import admin
from django import forms   
#from .models import GraphData
from import_export import resources, fields, widgets #Para los reportes
from import_export.widgets import ForeignKeyWidget #Para los reportes
from import_export.admin import ImportExportModelAdmin #Para los reportes
from .models import Alumnos, TelefonoAlumno, EmailAlumno
from .models import Profesor, TelefonoProfesor, EmailProfesor
from .models import Proveedor, TelefonoProveedor, EmailProveedor
from .models import Cursos, Materiales, MediosDidacticos
from .models import AlumnoCurso, ProfesorCurso, MaterialesCurso, MediosDidacticosCurso
from .models import MaterialesProfesor, ProfesorMediosDidacticos
from .models import ProveedorMateriales, ProveedorMediosDidacticos
#from .models import PDFConfig
import random
from datetime import datetime
#from django.shortcuts import render
#from django.urls import path
#from chartjs.views.lines import BaseLineChartView
#from django.contrib.auth.admin import GroupAdmin, UserAdmin
#from jazzmin.admin import JazzminModelAdminGroup, JazzminModelAdminUser
#from .models import Group, User
#from .models import Temas#Sin terminar los temas
#Reportes PDF
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


#Tener en cuenta list_display foreign key attributes para Listar datos de otro modelo

# Register your models here.
admin.site.site_header = "ACADEMIA DETECTA"

#Sin terminar los temas
""" class AdminThemeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user_theme = Temas.objects.filter(user=request.user).first()
            if user_theme:
                request.session["user_theme"] = user_theme.tema

        response = self.get_response(request)
        return response """

#Vistas de Alumnos en el sistema
#######################################################################################
#Clase para generar el reporte de los alumnos (Reporte)
class AlumnoResources(resources.ModelResource):
        curso = fields.Field(
                column_name='Curso',
                attribute='cursos',
                widget=widgets.ManyToManyWidget(Cursos, separator=',', field='nombre_curso')
        )

        carnet_alumno = fields.Field(column_name='Carnet', attribute='carnet_alumno')
        nombre_alumno = fields.Field(column_name='Nombre', attribute='nombre_alumno')
        username_alumno = fields.Field(column_name='Usuario', attribute='username_alumno')
        lugar_alumno = fields.Field(column_name='Lugar Nacimiento', attribute='lugar_alumno')
        nacionalidad_alumno = fields.Field(column_name='Nacionalidad', attribute='nacionalidad_alumno')
        fechanac_alumno = fields.Field(column_name='Fecha de nacimiento', attribute='fechanac_alumno')
        
        codigo_nivel_display = fields.Field(
                column_name='Nivel de escolaridad',
                attribute='get_codigo_nivel_display'
        )

        telefono_alumno = fields.Field(
                column_name='Teléfono',
                attribute='alumno',
                widget=ForeignKeyWidget(TelefonoAlumno, field='telefono_alumno')
        )

        def before_import_row(self, row, **kwargs):
                telefono = row["alumno"]
                TelefonoAlumno.objects.get_or_create(name=telefono, defaults={"Teléfono": telefono})

        #codigo_tipo_display = fields.Field(
        #        column_name='Tipo de Número',
        #        attribute='telefonoalumno__get_codigo_tipo_display',
        #        widget=ForeignKeyWidget(TelefonoAlumno, 'codigo_tipo')
        #)
        #codigo_empresa_display = fields.Field(
        #        column_name='Compañia del Número',
        #        attribute='telefonoalumno__get_codigo_empresa_display',
        #        widget=ForeignKeyWidget(TelefonoAlumno, 'codigo_empresa')
        #)

        class Meta:
                model = Alumnos
                exclude = ('id')
                fields = ('carnet_alumno', 'nombre_alumno', 'curso', 'username_alumno', 'lugar_alumno', 'nacionalidad_alumno', 'fechanac_alumno', 'codigo_nivel_display', 'telefono_alumno')#, 'codigo_tipo_display', 'codigo_empresa_display')
                export_order = fields

#Generar Carnet Alumno
def generar_carnet_alumno():
    # Generar el código del alumno
    # Utilizar el año actual
    year = datetime.now().year
    # Generar números aleatorios
    random_numbers = random.randint(1000, 9999)
    # Combinar los elementos en el código del alumno
    carnet = f"{year}-{random_numbers}ED"
    # Devolver el código del alumno
    return carnet

generar_carnet_alumno.short_description = "Generar código de alumno"




class AlumnoForm(forms.ModelForm):
        #carnet_alumno = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 11}))
        carnet_alumno = forms.CharField(initial=generar_carnet_alumno())

        def get_initial_for_field(self, field, field_name):
                if field_name == 'carnet_alumno':
                        return generar_carnet_alumno()
                return super().get_initial_for_field(field, field_name)
        

        """  # Definir los campos adicionales para el gráfico
        tipo_grafico = forms.ChoiceField(choices=[('barra', 'Gráfico de Barras'), ('pastel', 'Gráfico de Pastel')])
        datos_grafico = forms.ModelChoiceField(queryset=GraphData.objects.all())

        class Meta:
                model = Alumnos
                fields = '__all__' """




class TelefonoAlumnoInline(admin.TabularInline):
        model = TelefonoAlumno

class EmailAlumnoInline(admin.TabularInline):
        model = EmailAlumno   
  

class AlumnoAdmin(ImportExportModelAdmin):
        resource_class = AlumnoResources
        #change_form_template = 'graficos.html'

        form = AlumnoForm
        """  fieldsets = [
                ('Configuración del gráfico', {
                        'fields': ['tipo_grafico', 'datos_grafico'],
                }),
        ] """

        list_per_page = 8
        list_display=('carnet_alumno', 'nombre_alumno', 'username_alumno', 'nacionalidad_alumno', 'codigo_nivel')
        search_fields=('carnet_alumno', 'nombre_alumno')
        #list_filter=('fechanac_alumno', )
        list_filter=('nacionalidad_alumno', 'lugar_alumno')
        #filter_vertical = ('carnet_alumno', 'fechanac_alumno')
        #filter_horizontal = ('cursos', )
        inlines = [
                TelefonoAlumnoInline,
                EmailAlumnoInline,
        ] 

        #Generar carnet
        actions = [generar_carnet_alumno]

        #Generar pdf alumno
        def generate_pdf(modeladmin, request, queryset):
                # Obtener la plantilla HTML
                template = get_template('alumnos_template.html')
                
                # Datos para generar el PDF
                context = {
                        'alumnos': queryset
                }
                
                # Renderizar la plantilla HTML con los datos
                rendered_template = template.render(context)
                
                # Crear el objeto HttpResponse con el contenido PDF generado
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="alumnos.pdf"'
                
                # Convertir el contenido HTML a PDF
                pisa_status = pisa.CreatePDF(rendered_template, dest=response)
                
                # Si se generó correctamente el PDF, retornar el objeto HttpResponse
                if pisa_status.err:
                        return HttpResponse('Error al generar el PDF', status=500)
                return response


        actions = [generate_pdf]

        #def change_view(self, request, object_id, form_url='', extra_context=None):
                # Obtener los datos para el gráfico
        #        data = [10, 20, 30, 40, 50]

                # Renderizar el gráfico utilizando la plantilla chartjs.html
        #        chart = BaseLineChartView()
        #        chart.set_labels(["Uno", "Dos", "Tres", "Cuatro", "Cinco"])
        #        chart.add_dataset(data)
        #        chart.build()

        #        extra_context = extra_context or {}
        #        extra_context['chart'] = chart.get_context_data()

        #        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False


#Alumnos
admin.site.register(Alumnos, AlumnoAdmin)










#Vistas de Profesores en el sistema
#######################################################################################
#Clase para generar el reporte de los profesores (Reporte)
class ProfesorResources(resources.ModelResource):
        carnet_teacher = fields.Field(column_name='Carnet', attribute='carnet_teacher')
        nombre_teacher = fields.Field(column_name='Nombre', attribute='nombre_teacher')
        fechanac_teacher = fields.Field(column_name='Fecha de Nacimiento', attribute='fechanac_teacher')
        Numero_cedula = fields.Field(column_name='Número de Cédula', attribute='Numero_cedula')
        lugarOrigen_teacher = fields.Field(column_name='Lugar de Nacimiento', attribute='lugarOrigen_teacher')
        nacionalidad_teacher = fields.Field(column_name='Nacionalidad', attribute='nacionalidad_teacher')
        image = fields.Field(column_name='Imagen', attribute='image')
        descripcion_profesor = fields.Field(column_name='Descripción', attribute='descripcion_profesor')
        Referencias_profecionales = fields.Field(column_name='Referencias Profesionales', attribute='Referencias_profecionales')
        codigo_nivel = fields.Field(column_name='Nivel Académico', attribute='get_codigo_nivel_display')
        sexo = fields.Field(column_name='Género', attribute='get_sexo_display')

        #material = fields.Field(
        #        column_name='Material',
        #        attribute='materials',
        #        widget=widgets.ManyToManyWidget(Materiales, separator=',', field='nombre_material')
        #)

        #medio = fields.Field(
        #        column_name='Medio Didáctico',
        #        attribute='mediosdidactcos',
        #        widget=widgets.ManyToManyWidget(MediosDidacticos, separator=',', field='nombre_medio')
        #)

        class Meta:
                model = Profesor
                exclude = ('id', 'materiales', 'mediosdidacticos', 'cursos')
                export_order = ('carnet_teacher', 'nombre_teacher', 'fechanac_teacher', 'Numero_cedula', 'lugarOrigen_teacher', 'nacionalidad_teacher', 'image', 'descripcion_profesor', 'Referencias_profecionales', 'codigo_nivel', 'sexo')

#Generar Carnet Profesor
def generar_carnet_profesor():
    # Generar el código del profesor
    # Utilizar el año actual
    year = datetime.now().year
    # Generar números aleatorios
    random_numbers = random.randint(1000, 9999)
    # Combinar los elementos en el código del profesor
    carnet = f"{year}-{random_numbers}PD"
    # Devolver el código del profesor
    return carnet

generar_carnet_profesor.short_description = "Generar código de profesor"


class ProfesorForm(forms.ModelForm):
        #carnet_teacher = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 11}))
        carnet_teacher = forms.CharField(initial=generar_carnet_profesor())

        def get_initial_for_field(self, field, field_name):
                if field_name == 'codigo_profesor':
                        return generar_carnet_profesor()
                return super().get_initial_for_field(field, field_name)


class TelefonoProfesorInline(admin.TabularInline):
        model = TelefonoProfesor

class EmailProfesorInline(admin.TabularInline):
        model = EmailProfesor       

class ProfesorCursoInline(admin.TabularInline):
        model = ProfesorCurso
        extra = 1
        min_num = 0

class MaterialesProfesorInline(admin.TabularInline):
        model = MaterialesProfesor
        extra = 1
        min_num = 0


class ProfesorMediosDidacticosInline(admin.TabularInline):
        model = ProfesorMediosDidacticos
        extra = 1
        min_num = 0

class   ProfesorAdmin(ImportExportModelAdmin):
        resource_class = ProfesorResources
        form = ProfesorForm
        list_per_page = 8
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

        #Generar carnet profesor
        actions = [generar_carnet_profesor]

        #Generar pdf profesor
        def generate_pdf(self, request, queryset):
                template = get_template('profesor_template.html')
                context = {
                'profesores': queryset
                }
                rendered_template = template.render(context)
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="profesores.pdf"'
                pisa_status = pisa.CreatePDF(rendered_template, dest=response)
                if pisa_status.err:
                        return HttpResponse('Error al generar el PDF', status=500)
                return response

        generate_pdf.short_description = 'Generar PDF'

        actions = ['generate_pdf']

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False



#Profesores
admin.site.register(Profesor, ProfesorAdmin)











#Vistas de Proveedores en el sistema
#######################################################################################
#Clase para generar el reporte de los Proveedores (Reporte)
class ProveedorResources(resources.ModelResource):
        codigo_proveedor = fields.Field(column_name='Código Proveedor', attribute='codigo_proveedor')
        nombre_proveedor = fields.Field(column_name='Nombre del proveedor', attribute='nombre_proveedor')
        descripcion_proveedor = fields.Field(column_name='Descripción', attribute='descripcion_proveedor')
        calidad = fields.Field(column_name='Calidad', attribute='get_calidad_display')
        direccion = fields.Field(column_name='Dirección', attribute='direccion')
        observacion = fields.Field(column_name='Observaciones', attribute='observacion')

        material = fields.Field(
                column_name='Material',
                attribute='materials',
                widget=widgets.ManyToManyWidget(Materiales, separator=',', field='nombre_material')
        )

        medio = fields.Field(
                column_name='Medio Didáctico',
                attribute='mediosdidactcos',
                widget=widgets.ManyToManyWidget(MediosDidacticos, separator=',', field='nombre_medio')
        )

        class Meta:
                model = Proveedor
                exclude = ('id', 'materials', 'mediosdidactcos',)
                export_order = ('codigo_proveedor', 'nombre_proveedor', 'descripcion_proveedor', 'calidad', 'direccion', 'observacion', 'material', 'medio')

#Generar Código Proveedor
def generar_codigo_proveedor():
    # Generar el código del proveedor
    # Utilizar el año actual
    year = datetime.now().year
    # Generar números aleatorios
    random_numbers = random.randint(1000, 9999)
    # Combinar los elementos en el código del proveedor
    codigo = f"{year}-{random_numbers}PRD"
    # Devolver el código del proveedor
    return codigo

generar_codigo_proveedor.short_description = "Generar código de proveedor"


class ProveedorForm(forms.ModelForm):
        #codigo_proveedor = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 12}))
        codigo_proveedor = forms.CharField(initial=generar_codigo_proveedor())

        def get_initial_for_field(self, field, field_name):
                if field_name == 'codigo_proveedor':
                        return generar_codigo_proveedor()
                return super().get_initial_for_field(field, field_name)


class TelefonoProveedorInline(admin.TabularInline):
        model = TelefonoProveedor

class EmailProveedorInline(admin.TabularInline):
        model = EmailProveedor       

class ProveedorMediosDidacticosInline(admin.TabularInline):
        model = ProveedorMediosDidacticos
        extra = 1
        min_num = 0

class ProveedorMaterialesInline(admin.TabularInline):
        model = ProveedorMateriales
        extra = 1
        min_num = 0

class   ProveedorAdmin(ImportExportModelAdmin):
        resource_class = ProveedorResources
        form = ProveedorForm
        list_per_page = 8
        list_display=('codigo_proveedor', 'nombre_proveedor', 'calidad', 'direccion')
        search_fields=('codigo_proveedor', 'nombre_proveedor')
        list_filter=('nombre_proveedor', 'calidad')
        inlines = [
                TelefonoProveedorInline,
                EmailProveedorInline,
                ProveedorMediosDidacticosInline,
                ProveedorMaterialesInline,
        ]

        #Generar código proveedor
        actions = [generar_codigo_proveedor]

        #Generar pdf proveedor
        def generate_pdf(self, request, queryset):
                template = get_template('proveedor_template.html')
                context = {
                'proveedores': queryset
                }
                rendered_template = template.render(context)
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="proveedores.pdf"'
                pisa_status = pisa.CreatePDF(rendered_template, dest=response)
                if pisa_status.err:
                        return HttpResponse('Error al generar el PDF', status=500)
                return response

        generate_pdf.short_description = 'Generar PDF'

        actions = ['generate_pdf']

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False

#Proveedores
admin.site.register(Proveedor, ProveedorAdmin)










#Vistas de Cursos en el sistema
#######################################################################################
#Clase para generar el reporte de los cursos (Reporte)
class CursosResources(resources.ModelResource):
        codigo_curso = fields.Field(column_name='Código', attribute='codigo_curso')
        nombre_curso = fields.Field(column_name='Nombre', attribute='nombre_curso')
        fecha_inicio = fields.Field(column_name='Fecha de inicio', attribute='fecha_inicio')
        fecha_final = fields.Field(column_name='Fecha de finalización', attribute='fecha_final')
        numero_horas = fields.Field(column_name='Horas de duración', attribute='numero_horas')
        descripcion_cursos = fields.Field(column_name='Descripción', attribute='descripcion_cursos')
        observaciones_cursos = fields.Field(column_name='Observaciones', attribute='observaciones_cursos')
        especialidad = fields.Field(column_name='Especialidad', attribute='get_codigo_especialidad_display')

        class Meta:
                model = Cursos
                exclude = ('id',)
                fields = ('codigo_curso', 'nombre_curso', 'fecha_inicio', 'fecha_final', 'numero_horas', 'descripcion_cursos', 'observaciones_cursos', 'especialidad')
                export_order = fields

#Generar Código Curso
def generar_codigo_curso():
    # Generar el código del curso
    # Utilizar el año actual
    year = datetime.now().year
    # Generar números aleatorios
    random_numbers = random.randint(1000, 9999)
    # Combinar los elementos en el código del curso
    codigo = f"{year}-{random_numbers}CD"
    # Devolver el código del curso
    return codigo

generar_codigo_curso.short_description = "Generar código de curso"


class CursoForm(forms.ModelForm):
        #codigo_curso = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 11}))
        codigo_curso = forms.CharField(initial=generar_codigo_curso())

        def get_initial_for_field(self, field, field_name):
                if field_name == 'codigo_curso':
                        return generar_codigo_curso()
                return super().get_initial_for_field(field, field_name)


class MediosDidacticosCursoInline(admin.TabularInline):
        model = MediosDidacticosCurso
        extra = 1
        min_num = 0

class MaterialesCursoInline(admin.TabularInline):
        model = MaterialesCurso
        extra = 1
        min_num = 0


class AlumnoCursoInline(admin.TabularInline):
        model = AlumnoCurso  
        extra = 1
        min_num = 0

class  CursoAdmin(ImportExportModelAdmin):
        resource_class = CursosResources
        form = CursoForm
        list_per_page = 8
        list_display=('codigo_curso', 'nombre_curso', 'image', 'codigo_especialidad')
        search_fields=('codigo_curso', 'nombre_curso')
        list_filter=('fecha_inicio', 'fecha_final')
        #list_filter=('calidad')
        inlines = [
                MediosDidacticosCursoInline,
                MaterialesCursoInline,
                AlumnoCursoInline,
        ]

        #Generar código curso
        actions = [generar_codigo_curso]

        #Generar pdf cursos
        def generate_pdf(self, request, queryset):
                template = get_template('cursos_template.html')
                context = {
                'cursos': queryset
                }
                rendered_template = template.render(context)
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="cursos.pdf"'
                pisa_status = pisa.CreatePDF(rendered_template, dest=response)
                if pisa_status.err:
                        return HttpResponse('Error al generar el PDF', status=500)
                return response

        generate_pdf.short_description = 'Generar PDF'

        actions = ['generate_pdf']

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False

#Cursos
admin.site.register(Cursos, CursoAdmin)






#Vistas de Materiales en el sistema
#######################################################################################
#Clase para generar el reporte de los materiales (Reporte)
class MaterialesResources(resources.ModelResource):
        codigo_material = fields.Field(column_name='Código', attribute='codigo_material')
        nombre_material = fields.Field(column_name='Nombre', attribute='nombre_material')
        descripcion_material = fields.Field(column_name='Descripción', attribute='descripcion_material')
        cantidadMat = fields.Field(column_name='Cantidad', attribute='cantidadMat')
        precioMat = fields.Field(column_name='Precio', attribute='precioMat')
        unidad_MedidaMat = fields.Field(column_name='Unidad de medida', attribute='unidad_MedidaMat')
        fecha_caducidadMat = fields.Field(column_name='Fecha de caducidad', attribute='fecha_caducidadMat')
        fecha_compraMat = fields.Field(column_name='Fecha de compra', attribute='fecha_compraMat')
        costo_totalMat = fields.Field(column_name='Costo total', attribute='costo_totalMat')
        costo_unitarioMat = fields.Field(column_name='Costo unitario', attribute='costo_unitarioMat')

        curso = fields.Field(
                column_name='Curso',
                attribute='cursos',
                widget=widgets.ManyToManyWidget(Cursos, separator=',', field='nombre_curso')
        )

        class Meta:
                model = Materiales
                exclude = ('id')
                fields = ('codigo_material', 'nombre_material', 'descripcion_material', 'cantidadMat', 'precioMat', 'unidad_MedidaMat', 'fecha_caducidadMat', 'fecha_compraMat', 'costo_totalMat', 'costo_unitarioMat', 'cursos')
                export_order = fields

#Generar Código Material
def generar_codigo_material():
    # Generar el código del material
    # Utilizar el año actual
    year = datetime.now().year
    # Generar números aleatorios
    random_numbers = random.randint(1000, 9999)
    # Combinar los elementos en el código del material
    codigo = f"{year}-{random_numbers}MTD"
    # Devolver el código del material
    return codigo

generar_codigo_material.short_description = "Generar código de material"


class MaterialesForm(forms.ModelForm):
        #codigo_material = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 12}))
        codigo_material = forms.CharField(initial=generar_codigo_material())

        def get_initial_for_field(self, field, field_name):
                if field_name == 'codigo_material':
                        return generar_codigo_material()
                return super().get_initial_for_field(field, field_name)

class MaterialesAdmin(ImportExportModelAdmin):
        resource_class = MaterialesResources
        form = MaterialesForm
        list_per_page = 8
        list_display=('codigo_material', 'nombre_material', 'unidad_MedidaMat', 'costo_unitarioMat', 'costo_totalMat', 'cantidadMat')
        search_fields=('codigo_material', 'nombre_material')
        list_filter=('nombre_material', 'unidad_MedidaMat')
        list_filter=('fecha_compraMat', 'cantidadMat')

        #Generar código de material
        actions = [generar_codigo_material]

        #Generar pdf materiales
        def generate_pdf(self, request, queryset):
                template = get_template('materiales_template.html')
                context = {
                'materiales': queryset
                }
                rendered_template = template.render(context)
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="materiales.pdf"'
                pisa_status = pisa.CreatePDF(rendered_template, dest=response)
                if pisa_status.err:
                        return HttpResponse('Error al generar el PDF', status=500)
                return response

        generate_pdf.short_description = 'Generar PDF'

        actions = ['generate_pdf']

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False

#Materiales
admin.site.register(Materiales, MaterialesAdmin)








#Vistas de Medios Didácticos en el sistema
#######################################################################################
#Clase para generar el reporte de los medios didacticos (Reporte)
class MediosDidacticosResources(resources.ModelResource):
        codigo_medios = fields.Field(column_name='Código Medios Didácticos', attribute='codigo_medios')
        nombre_medio = fields.Field(column_name='Nombre del Medio Didáctico', attribute='nombre_medio')
        descripcion_medio = fields.Field(column_name='Descripción', attribute='descripcion_medio')
        cantidad = fields.Field(column_name='Cantidad', attribute='cantidad')
        precio = fields.Field(column_name='Precio del Producto', attribute='precio')
        unidad_Medida = fields.Field(column_name='Unidad de Medida', attribute='unidad_Medida')
        fecha_caducidad = fields.Field(column_name='Fecha de Caducidad del Producto', attribute='fecha_caducidad')
        fecha_compra = fields.Field(column_name='Fecha de la Compra del Producto', attribute='fecha_compra')
        costo_total = fields.Field(column_name='Costo Total', attribute='costo_total')
        costo_unitario = fields.Field(column_name='Costo Unitario', attribute='costo_unitario')
        estado_asignacion = fields.Field(column_name='Estado de Asignación', attribute='get_estado_asignacion_display')

        curso = fields.Field(
                column_name='Curso',
                attribute='cursos',
                widget=widgets.ManyToManyWidget(Cursos, separator=',', field='nombre_curso')
        )

        class Meta:
                model = MediosDidacticos
                exclude = ('id')
                export_order = ('codigo_medios', 'nombre_medio', 'descripcion_medio', 'cantidad', 'precio', 'unidad_Medida', 'fecha_caducidad', 'fecha_compra', 'costo_total', 'costo_unitario', 'estado_asignacion','curso')

#Generar Código Medio Didáctico
def generar_codigo_medio_didactico():
    # Generar el código del medio didáctico
    # Utilizar el año actual
    year = datetime.now().year
    # Generar números aleatorios
    random_numbers = random.randint(1000, 9999)
    # Combinar los elementos en el código del medio didáctico
    codigo = f"{year}-{random_numbers}MDD"
    # Devolver el código del medio didáctico
    return codigo

generar_codigo_medio_didactico.short_description = "Generar código de medio didáctico"


class MediosDidacticosForm(forms.ModelForm):
        #codigo_medios = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 12}))
        codigo_medios = forms.CharField(initial=generar_codigo_medio_didactico())

        def get_initial_for_field(self, field, field_name):
                if field_name == 'codigo_medio_didactico':
                        return generar_codigo_medio_didactico()
                return super().get_initial_for_field(field, field_name)

class MediosDidacticosAdmin(ImportExportModelAdmin):
        resource_class = MediosDidacticosResources
        form = MediosDidacticosForm
        list_per_page = 8
        list_display=('codigo_medios', 'nombre_medio', 'unidad_Medida', 'costo_unitario', 'costo_total', 'estado_asignacion')
        search_fields=('codigo_medios', 'nombre_medio')
        list_filter=('estado_asignacion', 'unidad_Medida')

        #Generar código de medio didáctico
        actions = [generar_codigo_medio_didactico]

        #Generar pdf medios didácticos
        def generate_pdf(self, request, queryset):
                template = get_template('medios_template.html')
                context = {
                'medios': queryset
                }
                rendered_template = template.render(context)
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="medios.pdf"'
                pisa_status = pisa.CreatePDF(rendered_template, dest=response)
                if pisa_status.err:
                        return HttpResponse('Error al generar el PDF', status=500)
                return response

        generate_pdf.short_description = 'Generar PDF'

        actions = ['generate_pdf']

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

#Custom Jazmin
#@admin.register(Group)
#class GroupAdmin(JazzminModelAdminGroup, GroupAdmin):
#    pass

#@admin.register(User)
#class UserAdmin(JazzminModelAdminUser, UserAdmin):
#    pass


#@admin.register(Group)
#class GroupAdmin(JazzminModelAdminGroup, GroupAdmin):
#    list_display = ('name', 'permissions')
#    list_filter = ('permissions',)
#    search_fields = ('name',)

#@admin.register(User)
#class UserAdmin(JazzminModelAdminUser, UserAdmin):
#    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
#    list_filter = ('is_staff',)
#    search_fields = ('username', 'email', 'first_name', 'last_name')


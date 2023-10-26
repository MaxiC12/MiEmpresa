from functools import cached_property
from time import timezone
from django.db import models
from ckeditor.fields import RichTextField

class Persona(models.Model):
    SEXO= [('M','Masculino'),
           ('F','Femenino'),
           ('X', 'Otro'),
           ]

    ESTADO_CIVIL= [('C','Casado'),
                   ('S','Soltero'),
                   ('V','Viudo'),
                   ('O','Otro'),
                   ]
    dni= models.CharField(max_length=8, verbose_name='D.N.I.', help_text='Ingrese sin puntos', blank=True, null=True)
    nombre= models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nac = models.DateField(max_length=6, verbose_name='Fecha de nacimiento',help_text='dia/mes/año')
    created = models.DateTimeField(auto_now_add=True) #cuando fue creado
    update = models.DateTimeField(auto_now_add=True)  #cuando fue actualizado
    sexo= models.CharField(max_length=10, choices=SEXO, default='F')
    estado_civil= models.CharField(max_length=8, choices=ESTADO_CIVIL, default='S')
    vive= models.BooleanField(default=True)
    foto = models.ImageField( 
        upload_to='media/imagenes/',  # Ruta donde se guardarán las imágenes
        verbose_name='Foto 4x4',  # Nombre descriptivo para la interfaz de administración
        default='media/imagenes/avatar.png',
        max_length=254)
    Email=models.EmailField(max_length=250, default='Ejemplo@gmail.com')
    legajo= RichTextField(default='legajo de persona')

    def _str_(self):
        return f'{self.apellido},{self.nombre}, fecha Nac{self.fecha_nac}'
    
    @cached_property
    def edad(self):
        edad=0
        if self.fecha_nac:
            dias_anual=365.2425
            edad=int((timezone.now().date()-self.fecha_nac).days / dias_anual)
        return edad

    class Meta:
        verbose_name='Persona'
        verbose_name_plural= 'Personas'
        ordering=('apellido','nombre')

class Contacto(models.Model):
    nombre= models.CharField(max_length=100)
    email= models.EmailField(max_length=250)
    mensaje= models.TextField(max_length=250, default="escriba su mensaje ")

    class Meta:
        verbose_name='Contacto'
        verbose_name_plural= 'Contactos'
            









# Create your models here.

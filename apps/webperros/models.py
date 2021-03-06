from django.db import models

# Create your models here.
class libro(models.Model):
    pk_libro = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    autor = models.CharField(max_length=50, null=False, blank=False)
    paginas = models.TextField(null=False,blank=False)
    fecha_de_lanzamiento= models.DateField(null=False,auto_now = False , auto_now_add = False)
    idioma= models.CharField(null=False, max_length=50, blank=False)
    disponibilidad= models.CharField(null=False, max_length=50, blank=False)
    precio= models.DecimalField(max_digits=5, decimal_places=2)
    img = models.URLField(max_length=8000, blank=False, null=False, default='https://i.postimg.cc/xjH36Tw2/2222222222.jpg')


    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'libros'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)

class categorias(models.Model):
    pk_categorias = models.AutoField(primary_key=True, null=False, blank=False)
    variedad = models.CharField(max_length=80,null=False, blank=False)
    editorial = models.CharField(max_length=80, null=False, blank=False)
    fk_libro = models.ForeignKey(libro, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['variedad']

    def __str__(self):
        return "{0}".format(self.variedad)
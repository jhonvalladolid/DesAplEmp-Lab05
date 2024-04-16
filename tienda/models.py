from django.db import models

# Create your models here.
class Categoria(models.Model):
  nombre = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.nombre
  
class Producto(models.Model):
  Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  nombre = models.CharField(max_length=200)
  precio = models.DecimalField(max_digits=6, decimal_places=2)
  stock = models.IntegerField(default=0)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.nombre
  
class Direccion(models.Model):
    nombre_calle = models.CharField(max_length=200)
    manzana = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    numero_lote = models.CharField(max_length=100)
    
    def __str__(self):
      return self.nombre_calle

  
class Cliente(models.Model):
  nombre = models.CharField(max_length=200)
  apellidos = models.CharField(max_length=200)
  dni = models.CharField(max_length=8)
  telefono = models.CharField(max_length=100)
  direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
  email = models.EmailField()
  f_nacimiento = models.DateField()
  f_publicacion = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.nombre
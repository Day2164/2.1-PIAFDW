from django.db import models

# Create your models here.

class producto(models.Model):
    ID_Producto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Material = models.CharField(max_length=50)
    Stock = models.IntegerField()
    Categoria = models.CharField(max_length=50)


    def __str__(self):
        return self.Nombre
    
class sucursale(models.Model):
    ID_Sucursal = models.AutoField(primary_key=True)
    Nombre_Sucursal = models.CharField(max_length=100)  
    Direccion = models.CharField(max_length=200)  
    Telefono = models.CharField(max_length=15)
    Horario = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_Sucursal
    
class empleado(models.Model):
    ID_Empleado = models.AutoField(primary_key=True)
    Nombre_Empleado = models.CharField(max_length=100)
    Puesto = models.CharField(max_length=50)
    Sucursal_asignada = models.ForeignKey(sucursale, on_delete=models.CASCADE)
    Correo = models.EmailField()
    Telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.Nombre_Empleado
    
class cliente(models.Model):
    ID_Cliente = models.AutoField(primary_key=True)
    Nombre_Cliente = models.CharField(max_length=100)
    Correo = models.EmailField()
    Telefono = models.CharField(max_length=15)
    Direccion = models.CharField(max_length=200)
    Metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_Cliente


    
    


    
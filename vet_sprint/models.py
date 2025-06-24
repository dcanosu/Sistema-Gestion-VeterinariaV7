
from django.db import models

class Propietario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100) 
    telefono = models.CharField(max_length=20) 
    direccion = models.CharField(max_length=255) 

    def __str__(self):
        return self.nombre 
    
    class Meta:
        verbose_name_plural = "Propietarios" 

class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100) 
    especie = models.CharField(max_length=50) 
    raza = models.CharField(max_length=50, blank=True, null=True) 
    edad = models.IntegerField()
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - {self.propietario.nombre}"

    class Meta:
        verbose_name_plural = "Mascotas" 

class Cita(models.Model): 
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    motivo = models.TextField() 
    diagnostico = models.TextField(blank=True, null=True) 
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='citas')

    def __str__(self):
        return f"Cita para {self.mascota.nombre} el {self.fecha.strftime('%d/%m/%Y')} - {self.motivo[:50]}..."
    
    class Meta:
        verbose_name_plural = "Citas" 
        ordering = ['fecha'] 
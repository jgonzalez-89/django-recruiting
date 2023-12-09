from django.db import models

class Transaccion(models.Model):
    hash = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    emisor = models.CharField(max_length=100)
    receptor = models.CharField(max_length=100)
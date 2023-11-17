from django.db import models
from variables.models import Variable

class Activo(models.Model):
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length=50)
    valor = models.FloatField(null=True, blank=True, default=None)
    unit = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)
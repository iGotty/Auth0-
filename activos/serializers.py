from rest_framework import serializers
from . import models


class ActivoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'variable','nombre',  'valor', 'unit', 'cantidad', 'time',)
        model = models.Activo
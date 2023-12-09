from rest_framework import serializers
from .models import Transaccion

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = '__all__'


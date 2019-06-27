from .models import OrdenPapel
from .models import OrdenSistema
from rest_framework import serializers


class OrdenPapelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenPapel
        fields = '__all__'

class OrdenSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenSistema
        fields = '__all__'

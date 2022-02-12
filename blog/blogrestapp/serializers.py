from rest_framework.serializers import ModelSerializer

from .models import Maqola, Rasm


class MaqolaSerializer(ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'


class RasmSerializer(ModelSerializer):
    class Meta:
        model = Rasm
        fields = '__all__'

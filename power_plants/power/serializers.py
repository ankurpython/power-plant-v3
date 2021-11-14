from rest_framework.serializers import ModelSerializer
from .models import PowerGenerator


class GeneratorSerializer(ModelSerializer):
    class Meta:
        model = PowerGenerator
        fields = '__all__'
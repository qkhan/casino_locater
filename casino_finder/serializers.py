from rest_framework import serializers
from .models import Casino

class CasinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casino
        fields = ('id', 'name', 'address')

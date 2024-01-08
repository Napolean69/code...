from rest_framework import serializers
from .models import txte, txteDetail

class txteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = txteDetail
        fields = '__all__'

class txteSerializer(serializers.ModelSerializer):
    details = txteDetailSerializer(many=True, read_only=True)

    class Meta:
        model = txte
        fields = '__all__'

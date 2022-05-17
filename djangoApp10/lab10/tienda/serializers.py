from rest_framework import serializers
from .models import Producto
 
 
class ProductoSerializer(serializers.ModelSerializer):
    codigo = serializers.IntegerField()
    descripcion = serializers.CharField()
    precio = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Producto
        fields = ('codigo', 'descripcion', 'precio')
 
    def create(self, validated_data):
        """
        Create and return a new `Producto` instance, given the validated data.
        """
        return Producto.objects.create(**validated_data)
 
    def update(self, instance, validated_data):
        """
        Update and return an existing `Producto` instance, given the validated data.
        """
        instance.codigo = validated_data.get('codigo', instance.codigo)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.save()
        return instance
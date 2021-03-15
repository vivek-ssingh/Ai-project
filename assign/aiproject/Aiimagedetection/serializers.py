from rest_framework import serializers
class Serialdata(serializers.Serializer):
     imgf=serializers.ImageField()
     xmlf=serializers.FileField()
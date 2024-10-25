from rest_framework import serializers
from .models import Task

class taskSerializer(serializers.ModelSerializer): #criando um serializers para o modelo task
    class Meta:
        model = Task #especificando a qual model pertence esse serializer
        fields = "__all__" #incluindo todos os campos do model para o serializer
        


from rest_framework import serializers
from .models import Student

def start_with_r(value):
     if value[0].lower() != 'r':
          raise serializers.ValidationError("Name should start with R!")
     
class StudentSerializer(serializers.ModelSerializer):
     class Meta: # when we want to go with default valdiations or mention in meta class for changes related to real_only => read_only_fields = ['name', 'roll']
          model = Student
          fields = ['id', 'name', 'roll', 'city']

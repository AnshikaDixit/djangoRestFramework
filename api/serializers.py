from rest_framework import serializers
from .models import Student

# implementation of model serializers

class StudentSerializer(serializers.ModelSerializer):
     class Meta:
          model = Student
          fields = ['id', 'name', 'roll', 'city']
    #create and update methods not required for model serializers, managed by it own




# implementation of serializers

# #Validators (P1)
# def start_with_r(value):
#      if value[0].lower() != 'r':
#           raise serializers.ValidationError("Name should start with R!")
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, validators=[start_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     def create(self, validate_data):
#         return Student.objects.create(**validate_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()  # Save the updated instance
#         return instance  # Return the updated instance
    
# #Field level validation (P2)
# def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError("Seat full!")
#         return value
    
# #Object level validation (P3)
# def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
#             raise serializers.ValidationError("City must be ranchi !")
#         return data
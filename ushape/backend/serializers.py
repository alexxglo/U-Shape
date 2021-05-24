from rest_framework import serializers
from backend.models import Calorielist
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class CalorielistSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=True, max_length=100)
    calories = serializers.CharField(required=True, allow_blank=True, max_length=100)
    fat = serializers.CharField(required=True, allow_blank=True, max_length=100)
    carbs = serializers.CharField(required=True, allow_blank=True, max_length=100)
    protein = serializers.CharField(required=True, allow_blank=True, max_length=100)
    sodium = serializers.CharField(required=True, allow_blank=True, max_length=100)
    calcium = serializers.CharField(required=True, allow_blank=True, max_length=100)
    iron = serializers.CharField(required=True, allow_blank=True, max_length=100)
    isType = serializers.CharField(required=True, allow_blank=True, max_length=100)
# we took shortcuts 
# class CalorielistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Calorielist
#         fields = ['id', 'name', 'calories', 'fat', 'carbs', 'protein', 'sodium', 'calcium', 'iron', 'isType']
    def create(self, validated_data):
        return Calorielist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('title', instance.name)
        instance.calories = validated_data.get('calories', instance.calories)
        instance.fat = validated_data.get('fat', instance.fat)
        instance.carbs = validated_data.get('carbs', instance.carbs)
        instance.protein = validated_data.get('protein', instance.protein)
        instance.sodium = validated_data.get('sodium', instance.sodium)
        instance.calcium = validated_data.get('calcium', instance.calcium)
        instance.iron = validated_data.get('iron', instance.iron)
        instance.isType = validated_data.get('isType', instance.isType)
        instance.save()
        return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
from rest_framework import serializers
from backend.models import Calorielist

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
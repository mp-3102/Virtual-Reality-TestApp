from rest_framework import serializers
from Testapp.models import Room_Type


class NumberSerializer(serializers.Serializer):
    Number = serializers.IntegerField(required=True)
    Price = serializers.FloatField(required=True)
    Type = serializers.ChoiceField(choices=Room_Type.Type_Choices)
    def update(self, instance, validated_data):
        instance.Number = validated_data.get('Number', instance.Number)
        instance.Price = validated_data.get('Price', instance.Price)
        instance.Type = validated_data.get('Type', instance.Type)
        return instance
    

    
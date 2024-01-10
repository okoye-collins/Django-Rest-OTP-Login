from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'phone_number']

    def validate(self, attrs):
        username = attrs.get('username', '')
        phone_number = attrs.get('phone_number', '')

        if len(phone_number) != 11:
            raise serializers.ValidationError(
                "The Phone number should be 11 digits.")

        if not username.isalnum():
            raise serializers.ValidationError(
                "The username should only contain alphanumeric character")

        return attrs

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
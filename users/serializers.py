from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password



AuthUserModel = get_user_model()

class RegisterSerializer(serializers.Serializer):
      username = serializers.CharField(required=True,max_length=255)
      email = serializers.EmailField(required=True)
      password = serializers.CharField(max_length=128, required=True)
      
      
      @staticmethod
      def validate_email(email):
          return email
      @staticmethod
      def validate_password(password):
          return password
        
      def create(self, validated_data):
          AuthUserModel.objects.create(
              username=validated_data['username'],
              email=validated_data['email'],
              password=make_password(validated_data['password']),
          )

        
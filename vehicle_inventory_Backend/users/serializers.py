from rest_framework import serializers
from .models import User, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                 'phone_number', 'is_active', 'is_staff', 'is_superuser', 
                 'date_joined', 'created_at', 'updated_at', 'profile']
        read_only_fields = ['id', 'date_joined', 'created_at', 'updated_at'] 
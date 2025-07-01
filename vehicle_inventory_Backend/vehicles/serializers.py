from rest_framework import serializers
from .models import Vehicle, VehicleType, VehicleMaintenance
from users.models import User

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff', 'is_superuser', 'date_joined']

class VehicleSerializer(serializers.ModelSerializer):
    vehicle_type = VehicleTypeSerializer(read_only=True)
    assigned_driver = UserSerializer(read_only=True)
    
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleMaintenanceSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)
    performed_by = UserSerializer(read_only=True)
    
    class Meta:
        model = VehicleMaintenance
        fields = '__all__' 
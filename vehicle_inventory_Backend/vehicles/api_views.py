from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Vehicle, VehicleType, VehicleMaintenance
from .serializers import VehicleSerializer, VehicleTypeSerializer, VehicleMaintenanceSerializer

# Add DjangoModelPermissions for per-user permission enforcement
from rest_framework.permissions import DjangoModelPermissions

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions]
    
    def get_queryset(self):
        queryset = Vehicle.objects.all()
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class VehicleMaintenanceViewSet(viewsets.ModelViewSet):
    queryset = VehicleMaintenance.objects.all()
    serializer_class = VehicleMaintenanceSerializer
    permission_classes = [DjangoModelPermissions]
    
    def get_queryset(self):
        queryset = VehicleMaintenance.objects.all()
        vehicle_id = self.request.query_params.get('vehicle', None)
        if vehicle_id:
            queryset = queryset.filter(vehicle_id=vehicle_id)
        return queryset 
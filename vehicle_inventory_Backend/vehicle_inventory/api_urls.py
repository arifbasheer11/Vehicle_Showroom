from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from vehicles.api_views import VehicleViewSet, VehicleTypeViewSet, VehicleMaintenanceViewSet
from users.api_views import UserViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'vehicle-types', VehicleTypeViewSet)
router.register(r'maintenance', VehicleMaintenanceViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    # JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API endpoints
    path('', include(router.urls)),
] 
from django.urls import path, include
from .views import employees_home, EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', employees_home, name='employees_home'),
    path('', include(router.urls)),
] 
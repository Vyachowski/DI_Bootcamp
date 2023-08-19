from django.urls import path
from .views import (
    RentalList, RentalDetail, CustomerList, CustomerAdd,
    VehicleList, VehicleDetail, VehicleAdd,
    StationList, StationDetail, StationDistribution, StationDistribute
)

urlpatterns = [
    path('rent/rental/', RentalList.as_view(), name='rental-list'),
    path('rent/rental/<int:pk>/', RentalDetail.as_view(), name='rental-detail'),
    
    path('rent/customer/', CustomerList.as_view(), name='customer-list'),
    path('rent/customer/add/', CustomerAdd.as_view(), name='customer-add'),
    
    path('rent/vehicle/', VehicleList.as_view(), name='vehicle-list'),
    path('rent/vehicle/<int:pk>/', VehicleDetail.as_view(), name='vehicle-detail'),
    path('rent/vehicle/add/', VehicleAdd.as_view(), name='vehicle-add'),
    
    path('rent/station/', StationList.as_view(), name='station-list'),
    path('rent/station/<int:pk>/', StationDetail.as_view(), name='station-detail'),
    path('rent/station/distribution/', StationDistribution.as_view(), name='station-distribution'),
    path('rent/station/distribute/', StationDistribute.as_view(), name='station-distribute'),
]
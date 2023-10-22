from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, VehicleType, VehicleSize, Vehicle, Rental, RentalRate, RentalStation, Address, VehicleAtRentalStation
from .serializers import (
    AddressSerializer, CustomerSerializer, VehicleTypeSerializer, VehicleSizeSerializer,
    VehicleSerializer, RentalSerializer, RentalRateSerializer,
    RentalStationSerializer, VehicleAtRentalStationSerializer
)
from rest_framework.permissions import AllowAny


# Create your views here.
class RentalList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        rentals = Rental.objects.all().order_by('return_date', 'rental_date')
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to retrieve, update, and delete a specific rental
class RentalDetail(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Rental.objects.get(pk=pk)
        except Rental.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        rental = self.get_object(pk)
        serializer = RentalSerializer(rental)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rental = self.get_object(pk)
        serializer = RentalSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rental = self.get_object(pk)
        rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# View to list customers
class CustomerList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        customers = Customer.objects.all().order_by('last_name', 'first_name')
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

# View to add a new customer
class CustomerAdd(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to list vehicles
class VehicleList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

# View to add a new vehicle
class VehicleAdd(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehicleDetail(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vehicle = self.get_object(pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# View to list rental stations
class StationList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        stations = RentalStation.objects.all()
        serializer = RentalStationSerializer(stations, many=True)
        return Response(serializer.data)

# View to display, update, or delete a specific station
class StationDetail(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return RentalStation.objects.get(pk=pk)
        except RentalStation.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        station = self.get_object(pk)
        serializer = RentalStationSerializer(station)
        return Response(serializer.data)

class StationDistribution(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        stations = RentalStation.objects.all()
        total_vehicles = sum(station.capacity for station in stations)
        average_vehicles_per_station = total_vehicles / len(stations) if len(stations) > 0 else 0
        return Response({'average_vehicles_per_station': average_vehicles_per_station})

class StationDistribute(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        stations = RentalStation.objects.all()
        vehicles_at_station = 10
        total_vehicles = len(stations) * vehicles_at_station
        vehicles_per_station = total_vehicles // len(stations)

        for station in stations:
            station.capacity = vehicles_per_station
            station.save()

        return Response({'message': 'Vehicles distributed successfully'})
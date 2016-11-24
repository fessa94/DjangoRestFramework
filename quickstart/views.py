from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import FlavourSerializer, VendorSerializer, ManufacturerSerializer


from .models import Shisha, Manufacturer, Vendor

class FlavourViewSet(viewsets.ModelViewSet):
    queryset = Shisha.objects.all()
    serializer_class = FlavourSerializer
    def get_queryset(self):

        queryset = Shisha.objects.all()
        flavour = self.request.query_params.get('flavour', None)
        if flavour is not None:
            queryset = queryset.filter(flavour=flavour)
        return queryset

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

    def get_queryset(self):

        queryset = Manufacturer.objects.all()
        manufacturer = self.request.query_params.get('manufacturer', None)
        if manufacturer is not None:
            queryset = queryset.filter(name=name)
        return queryset

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get_queryset(self):

        queryset = Vendor.objects.all()
        vendor = self.request.query_params.get('vendor', None)
        if vendor is not None:
            queryset = queryset.filter(name=name)
        return queryset


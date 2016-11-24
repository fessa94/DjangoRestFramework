from rest_framework import serializers

from .models import Shisha, Manufacturer, Vendor

class FlavourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shisha
        fields = ('flavour', 'manufacturer', 'quantity', 'strength')

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Manufacturer
		fields = ('name', 'vendor', 'rating', 'address')


class VendorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Vendor
		fields = ('name', 'address')



from models import Location, State, Nhdarea
from rest_framework import serializers


# Serializers

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'longitude', 'latitude')

class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ['name']


class NhdareaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nhdarea
        fields = ('ogc_fid','shape_area', 'areasqkm', 'resolution', 'fdate', 'gnis_name', 'shape_leng')
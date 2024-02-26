from rest_framework import serializers
from .models import *

class JobrequestSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source='status.name', read_only=True)
    place_name = serializers.CharField(source='place.name', read_only=True)
    rsponsible_person_name = serializers.CharField(source='rsponsible_person.name', read_only=True)
    class Meta:
        model = Jobrequest
        fields = "__all__"

class JobrequestSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Jobrequest
        fields = ['status']

class JobstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobstatus
        fields = "__all__"

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"

class RsponsiblePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsponsiblePerson
        fields = "__all__"
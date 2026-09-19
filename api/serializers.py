from rest_framework import serializers
from .models import Farmer, HarvestLog, GroupLeader
from .models import Driver
from .models import Trip

class GroupLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupLeader
        fields = '__all__'

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class HarvestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestLog
        fields = '__all__'
from .models import TransportCompany

class TransportCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportCompany
        fields = '__all__'
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
from .models import MarketPost

class MarketPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketPost
        fields = '__all__'
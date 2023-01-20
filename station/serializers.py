from dataclasses import fields
from rest_framework import serializers
from account.models import User
from area.serializers import AreaSerializer
from .models import Station
from city.serializers import CitySerializer
from state.serializers import StateSerializer
# from user.ser

class StationSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        ret = super(StationSerializer,self).to_representation(instance)

        if "city" in ret:
            ret["city_name"] = CitySerializer(instance.city).data["city_name"]
        
        if "state" in ret:
            ret["state_name"] = StateSerializer(instance.state).data["state_name"]

        if "area" in ret:
            ret["area_name"] = AreaSerializer(instance.area).data["area_name"]
        
        
        
        return ret

    def create(self, validated_data):
        req = self.context["request"]
        user = req.user.id
        station = Station.objects.create(**validated_data, created_by=user)
        return station

    class Meta:
        model = Station
        fields = '__all__'
        


# class StationRegistrationSerializer(serializers.ModelSerializer):
    
#     station_name = serializers.CharField(max_length=50)
#     station_address = serializers.CharField(max_length=255)
#     connectors = serializers.CharField(max_length=50)
#     available_time = serializers.TimeField()
#     user_type = serializers.ForeignKey(User, on_delete=serializers.CASCADE)

#     class Meta:
#         model = Station
#         fields = '__all__'
    
#     def validate(self, attrs):

#         if attrs['user_type'] != attrs['owner']:
#             raise serializers.ValidationError({"user_type": "Password fields didn't match."})
        
#         return attrs

#     def create(self, validated_data):
#         station = Station.objects.create(
#             station_name=validated_data['station_name'],
#             station_address=validated_data['station_address'],
#             connectors=validated_data['connectors'],
#             available_time=validated_data['available_time'],
        
#         )

#         return station


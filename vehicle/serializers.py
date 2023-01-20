from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['vehicle_number'] != data['vehicle_number']:
            raise serializers.ValidationError("Number is alreday exits")
        
        return data

    class Meta:
        model = Vehicle
        fields = '__all__'
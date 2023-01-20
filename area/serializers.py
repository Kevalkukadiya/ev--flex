from django.db.models import fields
from rest_framework import serializers
from .models import Area
from city.serializers import CitySerializer
from state.serializers import StateSerializer
from django.db.models import Q

class AreaSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super(AreaSerializer,self).to_representation(instance)

        if "city" in ret:
            ret["city_name"] = CitySerializer(instance.city).data["city_name"]
        
        if "state" in ret:
            ret["state_name"] = StateSerializer(instance.state).data["state_name"]


        return ret
    
    def validate(self, data):
        area_name = data.get('area_name')

        city = data.get('city')
        duplicate_area = Area.objects.filter(deleted=0, area_name__iexact=area_name, city_id=city)

        if self.partial:
            duplicate_area = duplicate_area.filter(~Q(pk=self.instance.area_id)).first()
        else:
            duplicate_area = duplicate_area.first()

        if duplicate_area != None:
            raise serializers.ValidationError("area already exist.")

        return data

    area_id = serializers.IntegerField(read_only=True)

        
    class Meta:
        model = Area
        fields = '__all__'



from django.db.models import fields
from rest_framework import serializers
from .models import City
from state.serializers import StateSerializer
from django.db.models import Q


class CitySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super(CitySerializer,self).to_representation(instance)

        if "state" in ret:
            ret["state_name"] = StateSerializer(instance.state).data["state_name"]

        return ret
        
    
    def validate(self, data,request):
        city_name = data.get('city_name')
        state_id = data.get('state')

        duplicate_city = City.objects.filter(deleted=0, city_name__iexact=city_name, state_id=state_id)

        if self.praticular:
            city = city.objects.filter(state_id=request.user)
        else:
            raise serializers.ValidationError("This State City does not exist")
         
        if self.partial:
            duplicate_city = duplicate_city.filter(~Q(pk=self.instance.city_id)).first()
        else:
            duplicate_city = duplicate_city.first()

        if duplicate_city != None:
            raise serializers.ValidationError("city already exist.")

        return data

    city_id = serializers.IntegerField(read_only=True)


    class Meta:
        model = City
        fields = '__all__'



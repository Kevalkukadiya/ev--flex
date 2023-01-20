from rest_framework import serializers
from slot.models import Slot
from station.serializers import StationSerializer


class SlotSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super(SlotSerializer, self).to_representation(instance)

        if "station" in ret:
            ret["station_name"] = StationSerializer(instance.station).data["station_name"]

       
        return ret
    
    def create(self, validated_data):
        req = self.context["request"]
        user = req.user.id
        print(user)
        slot = Slot.objects.create(**validated_data, created_by=user)
        return slot
    
    class Meta:
        model = Slot
        fields = "__all__"

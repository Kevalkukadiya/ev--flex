from urllib import request
from django import forms
from station.models import Station
from slot.models import Slot

CURRENT_STATUS_CHOICE = (
        ("AVAILABLE", "AVAILABLE"),
        ("OCCUPIED", "OCCUPIED")
    )
    
class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ('slot_name', 'per_unit_price', 'current_status','station')

    def clean(self):
    
        # data from the form is fetched using super function
        
        super(SlotForm, self).clean()
        
        station = Station.objects.filter(created_by=request.user.user_id)

        return station
       
    #     if Station.objects.filter(user_id=request.user):
    #         self.error_class([
    #             "This email address is already in use. Please supply a different email address."])
        

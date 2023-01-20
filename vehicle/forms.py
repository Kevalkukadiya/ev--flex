from django import forms
from vehicle.models import Vehicle

TYPE_CHOICE = (
        ("TWO-WHEELER", "TWO-WHEELER"),
        ("THREE-WHEELER", "THREE-WHEELER"),
        ("FOUR-WHEELER","FOUR-WHEELER")
    )

MANUFACTURE_COMPANY = (
        ("TATA", "TATA"),
        ("HYUNDAI", "HYUNDAI"),
        ("MG", "MG"),
        ("KIA", "KIA"),
        ("BMW", "BMW"),
        ("AUDI", "AUDI"),
        ("JAGUAR", "JAGUAR"),
        ("PORSCHE", "PORSCHE"),
        ("MERCEDES-BENZ", "MERCEDES-BENZ"),
        ("MINI COOPER", "MINI COOPER"),
        ("HERO ELECTRIC", "HERO ELECTRIC"),
        ("OLA ELECTRIC", "OLA ELECTRIC"),
        ("ATHER ENERGY", "ATHER ENERGY"),
        ("MAHINDRA ELECTRIC", "MAHINDRA ELECTRIC"),
        ("TVS", "TVS"),
        ("BAJAJ", "BAJAJ"),
        ("REVOLAT", "REVOLAT"),
        ("AMPERE EVS", "AMPERE EVS"),
        ("OKINAWA", "OKINAWA")

    )

class CreateVehicleForm(forms.ModelForm):
    vehicle_type= forms.CharField(required = True,label='Chocie your Vehicle type', widget=forms.Select(choices=TYPE_CHOICE))
    manufacture_company= forms.CharField(required=True, widget=forms.Select(choices=MANUFACTURE_COMPANY))
    model_name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    vehicle_number= forms.CharField(min_length=13,required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Vehicle
        fields = ('model_name', 'vehicle_type', 'manufacture_company', 'vehicle_number')



class UpdateVehicleForm(forms.ModelForm):
    
    vehicle_type= forms.CharField(required = True,label='Chocie your Vehicle type', widget=forms.Select(choices=TYPE_CHOICE))
    manufacture_company= forms.CharField(required=True, widget=forms.Select(choices=MANUFACTURE_COMPANY))
    model_name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    vehicle_number= forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Vehicle()
        fields = ('model_name', 'vehicle_type', 'manufacture_company', 'vehicle_number')

class vehicleform(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields="__all__"
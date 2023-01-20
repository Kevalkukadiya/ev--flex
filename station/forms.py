from django import forms
from city.models import City
from area.models import Area
from station.models import Station
from . import models

STATUS_CHOICE =  (
        ("ACTIVE", "ACTIVE"),
        ("INACTIVE", "INACTIVE")
        )

DAY_CHOICE =  (
        ("MONDAY", "MONDAY"),
        ("Tuesday", "TUESDAY"),
        ("WEDNESDAY", "WEDNESDAY"),
        ("THURSDAY", "THURSDAY"),
        ("FRIDAY", "FRIDAY"),
        ("SATURDAY", "SATURDAY"),
        ("SUNDAY", "SUNDAY"),
        ("ALL DAY", "ALL DAY")
    )

class CreateStationForm(forms.ModelForm):
    
    station_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    station_address = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    connectors = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    status = forms.CharField(required = True,label='Chocie your Vehicle type', widget=forms.Select(choices=STATUS_CHOICE))
    start_time = forms.CharField(required=True, widget=forms.TimeInput(attrs={'class':'form-control'}))
    end_time = forms.CharField(required=True, widget=forms.TimeInput(attrs={'class':'form-control'}))
    open_day = forms.ChoiceField(required = True,label='Chocie your Vehicle type', widget=forms.Select(choices=DAY_CHOICE))

    class Meta:
        model = Station
        fields = ('station_name', 'station_address','connectors','status', 'start_time','end_time','open_day')


class UpdateStationForm(forms.ModelForm):
    
    station_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    station_address = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    connectors = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    status = forms.CharField(required = True,label='Chocie your Vehicle type', widget=forms.Select(choices=STATUS_CHOICE))
    start_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'class':'form-control'}))
    end_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'class':'form-control'}))
    open_day = forms.ChoiceField(required = True,label='Chocie your Vehicle type', widget=forms.Select(choices=DAY_CHOICE))

    class Meta:
        model = Station
        fields = ('station_name', 'station_address','connectors','status', 'start_time','end_time','open_day')



class stationform(forms.ModelForm):
    class Meta:
        model=Station
        fields= ('station_name', 'station_address','connectors','status', 'start_time',
                'end_time','open_day', 'state', 'city', 'area')

      
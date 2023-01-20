import json

from django.http import JsonResponse
from area.models import Area
from city.models import City
from station.forms import  stationform
from .models import Station
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect,render,reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  CreateView


# ==================================== Create Station ============================================

class StationCreateView(LoginRequiredMixin, CreateView):
    model = Station
    fields = ('station_name', 'station_address','connectors','status', 'start_time','end_time','open_day', 
                'state', 'city', 'area')
    
    template_name = 'add_station.html'
    success_message = "Successfully Changed Your Password"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('view_station')

# ==================================== View Station ============================================

@login_required
def view_station(request):
    station=Station.objects.filter(user_id=request.user)
    return render(request,'view_station.html',{'station':station})

# ==================================== Update Station ============================================

@login_required
def edit_station(request, id):
    station = Station.objects.get(station_id=id)
    form = stationform(instance=station)

    if request.method == 'POST':
        form = stationform(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return redirect('view_station')

    context = {
        'station': station,
        'form': form,
    }
    return render(request, 'update_station.html', context)

# ==================================== Delete Station ============================================

@login_required
def delete_station(request,pk):   
        Station.objects.filter(station_id=pk).delete()
        messages.success(request, 'Your Station is Delete successfully')
        return redirect('view_station')


# @login_required
# def station_view(request):
#     station= Station.objects.filter(user_type_id=request.user)
#     return render(request,'owner/view_station.html',{'station':station})


# @api_view(['POST'])
# def create_station(request):
#     data = {}
#     if request.method == "POST":
#         station = Station()
#         serializer = StationSerializer(station, data=request.data)

#         if Station.objects.filter(**request.data).exists():
#             raise serializers.ValidationError('This Station is Already Exists')
    
#         if serializer.is_valid():
#             serializer.save()
#             data["success"] = True
#             data["msg"] = "Station upload Successfully"
#             data["data"] = serializer.data
#             return Response(data=data, status=status.HTTP_201_CREATED)

#         data["success"] = False
#         data["msg"] = {err_obj: str(serializer.errors[err_obj][0]) for err_obj in serializer.errors}
#         data["data"] = serializer.data
#         return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    

# @api_view(['POST'])
# def update_station(request, pk):
#     data={}
#     station = Station.objects.get(station_id=pk)
#     serializer = StationSerializer(instance=station, data=request.data)

#     if Station.objects.filter(**request.data).exists():
#         raise serializer.ValidationError('This Station is Already exists')
        
#     if serializer.is_valid():
#         serializer.save()
#         data["success"] = True
#         data["msg"] = "Data upload Successfully"
#         data["data"] = serializer.data
#         return Response(data=data, status=status.HTTP_201_CREATED)


#     data["success"] = False
#     data["msg"] = {err_obj: str(serializer.errors[err_obj][0]) for err_obj in serializer.errors}
#     data["data"] = serializer.data
#     return Response(data=data, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def view_station(request, id=None):
#     data = {}

#     try:
#         if id:
#             station = Station.objects.filter(pk=id, deleted=0)
#         else:
#             station = Station.objects.filter(deleted=0)
#         data["total_record"] = len(station)

#     except Station.DoesNotExist:
#         data["succes"] = False
#         data["msg"] = "Record Does not exist"
#         data["data"] = []
#         return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

#     if request.method == "GET":
#         serializer = StationSerializer(station, many=True)
#         data["succes"] = True
#         data["msg"] = "OK"
#         data["data"] = serializer.data
#         return Response(data=data, status=status.HTTP_200_OK)


# @api_view(['DELETE'])
# def delete_station(request, pk):
#     station = Station.objects.get(station_id=pk)
#     station.delete()

#     return Response('Station is Delete Succefully')

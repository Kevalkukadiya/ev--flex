from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from slot.models import Slot
from slot.serializers import SlotSerializer
from django.contrib.auth.decorators import login_required
from slot.forms import SlotForm
from django.contrib import messages

from django.shortcuts import redirect,render,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  CreateView,ListView
from station import models

from station.models import Station
from django.shortcuts import  get_object_or_404


# Create your views here.
@login_required  
def slot_create(request, **kwargs):  
    form = SlotForm(request.POST or None)  
    Station.objects.filter(created_by=request.user.user_id)

    # print(request.user.user_id)
    # station = Station.objects.filter(station_id=request.user.user_id)
 
    # station = Slot.objects.filter(station=request.user.user_id, created_by=request.user.user_id
    #                     )
    
    context = {
        'form': form,
              }

    if form.is_valid():  
        slot = form.save(commit=False)  
        slot.user = request.user  
        slot.created_by = request.user
        slot.save()  
        messages.success(request, 'Your Slot is add successfully')
        return redirect('view_slot')  

    return render(request, 'add_slot.html', context)  
  

# class SlotCreateView(LoginRequiredMixin, CreateView):
    
    
#     # queryset = Station.objects.get(user_id=user)
    
#     # station = Station.objects.filter(user_id=request.user)
    
#     model = Slot
#     fields = ('slot_name', 'per_unit_price', 'current_status','station')
    
#     template_name = 'add_slot.html'

    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
    
#     def get_success_url(self):
#         return reverse('view_slot')


@login_required

def view_slot(request):
    
    slot = Slot.objects.filter(user_id=request.user)
    context = {
        'slot': slot,
              }
    return render(request,'view_slot.html',context)


@login_required
def edit_slot(request, id):
    slot = Slot.objects.get(slot_id=id)
    form = SlotForm(instance=slot)

    if request.method == 'POST':
        form = SlotForm(request.POST, instance=slot)
        if form.is_valid():
            form.save()
            return redirect('view_slot')
    context = {
        'slot': slot,
        'form': form,
    }
    return render(request, 'update_slot.html', context)



# @api_view(['POST'])
# def create_slot(request):
#     data = {}
#     if request.method == "POST":
#         slot = Slot()
#         serializer = SlotSerializer(slot, data=request.data)

#         if Slot.objects.filter(**request.data).exists():
#             raise serializers.ValidationError('This Slot is Already Exists')

#         if serializer.is_valid():
#             serializer.save()
#             data["success"] = True
#             data["msg"] = "Slot upload Successfully"
#             data["data"] = serializer.data
#             return Response(data=data, status=status.HTTP_201_CREATED)
  
#         data["succes"] = False
#         data["msg"] = {err_obj: str(serializer.errors[err_obj][0]) for err_obj in serializer.error}
#         data["data"] = serializer.data
#         return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def view_slot(request, id=None):
#     data = {}
#     try:
#         if id:
#             slot = Slot.objects.filter(pk=id, deleted=0)
#         else:
#             slot = Slot.objects.filter(deleted=0)
#         data["total_record"] = len(slot)

#     except Slot.DoesNotExist:
#         data["succes"] = False
#         data["msg"] = "Record Does nit exist"
#         data["data"] = []
#         return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "GET":
#         serializer = SlotSerializer(slot, many=True)
#         data["succes"] = True
#         data["msg"] = "OK"
#         data["data"] = serializer.data
#         return Response(data=data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def update_slot(request, pk):
#     data = {}
#     slot = Slot.objects.get(slot_id=pk)
#     serializer = SlotSerializer(instance=slot, data=request.data)

#     if Slot.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This Slot is Alreay exists')

#     if serializer.is_valid():
#         serializer.save()
#         data["success"] = True
#         data["msg"] = "Slot update Successfully"
#         data["data"] = serializer.data
#         return Response(data=data, status=status.HTTP_201_CREATED)
    
#     data["success"] = False
#     data["msg"] =  {err_obj: str(serializer.errors[err_obj][0]) for err_obj in serializer.error}
#     data["data"] = serializer.data
#     return Response(data=data, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['DELETE'])
# def delete_slot(request, pk):
#     slot = Slot.objects.get(slot_id=pk)
#     slot.delete()

#     return Response('Slot is Delete Succefully')

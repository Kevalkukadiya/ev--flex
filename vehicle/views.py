from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from vehicle.forms import CreateVehicleForm,  UpdateVehicleForm
from django.contrib import messages
from vehicle.models import Vehicle

# ================================ Create Vehicle =============================================
@login_required
def add_vehicle(request):
    form = CreateVehicleForm()
    vehicle = None

    if request.method =='POST':
        form=CreateVehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            messages.success(request, 'Your vehicle is add successfully')
            return redirect('home')

    context = {'form':form}
    return render(request,'add_vehicle.html',context)

# ============================== View Vehicle =========================================
@login_required
def view_vehicle(request):
    vehicle=Vehicle.objects.filter(user=request.user)
    return render(request,'view_vehicle.html',{'vehicle':vehicle})

#==================================== Update Vehicle ===========================================

@login_required
def edit_vehicle(request, id):
    vehicle = Vehicle.objects.get(vehicle_id=id)
    form = UpdateVehicleForm(instance=vehicle)

    if request.method == 'POST':
        form = UpdateVehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'vehicle': vehicle,
        'form': form,
    }
    return render(request, 'edit_vehicle.html', context)

#==================================== Delete Vehicle =========================================

@login_required
def delete(request,pk):   
        Vehicle.objects.filter(vehicle_id=pk).delete()
        messages.success(request, 'Your vehicle is Delete successfully')
        return redirect('view_vehicle')
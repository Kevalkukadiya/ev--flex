from argparse import _CountAction
from django.shortcuts import HttpResponseRedirect, render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.urls import reverse
from account.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout

from account.models import User

from account import forms
from account.serializers import UserLoginSerializer



####################index#######################################
# Generate Token Manually


def home(request):
    return render(request, "user/user_home.html")

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'homepage/about.html', {})

def contact(request):
    return render(request, 'homepage/contact.html', {})

def chargepoint(request):
    return render(request, 'user/addchargepoint.html', {})

def service(request):
    return render(request, 'homepage/service.html', {})

def notfound(request):
    return render(request,'homepage/404.html')


# ============= User Register Here =========================================================================================================================

def register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password= form.cleaned_data.get('confirm_password')
            user = authenticate(email=email, password=password, confirm_password=confirm_password)
            # login(request, user)
                        
            return redirect("login")

    else:
        form = UserRegisterForm()
    return render(request, 'user/user_register.html',  {'form': form})

# ============================= Admin Register here ================================================================================

def admin_register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            # login(request, user)
            return redirect('login')
            # return render(request, "index.html")
    else:
        form = UserRegisterForm()
    return render(request, 'owner/admin_register.html',  {'form': form})


# ============= Login Here =========================================
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required   
from django.contrib import messages
from django.template import RequestContext
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email = email, password =password)
        print(user)
        if user is not None:
            login(request,user)    
            if user.user_type == "CUSTOMER":
                return render(request, "user/user_home.html")

            if user.user_type == "OWNER":
                return render(request, "homepage/owner_home.html")            

        else:
            messages.warning(request,'Email and Password does not match')
            return redirect('login')
    return render(request,'user/login.html')


      
            
   

# ============= Profile Information  Here =========================================

from .forms import   UpdateUserForm

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('home')
    else:
        user_form = UpdateUserForm(instance=request.user)
        
    return render(request, 'user/edit_profile.html', {'user_form': user_form})




# ============= Password Change  Here =========================================

from django.contrib.auth.views import  PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user/password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')


# ============= Log-out Here =========================================

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")


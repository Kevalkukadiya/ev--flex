"""user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from account import views
from account import views as user_views
from account.views import  ChangePasswordView, profile

admin.site.site_header = 'EV Flex Admin'
admin.site.index_title = 'Customization App'




urlpatterns = [
    path('evflexadmin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('', user_views.index, name='index'),
    # path('', user_views.chargepoint, name='chargepoint'),
    path('homepage/about.html', views.about, name="about"),
    path('homepage/contact.html', views.contact, name="contact"),
    path('user/addchargepoint.html', views.chargepoint, name="chargepoint"),
    path('404', views.notfound,name='index'),
    
    path('service.html', views.service, name="service"),
    path('state/',include("state.urls")),
    path('city/',include("city.urls")),
    path('area/',include("area.urls")),
    path('slot/',include("slot.urls")),
    path('station/',include("station.urls")),
    path('vehicle/', include("vehicle.urls")),
    
#====================== USer Realated Path ========================================== 

   	path('register/',  views.register_request, name ='register'),
   	path('admin_register/',  views.admin_register_request, name ='admin_register'),
    path('login/', views.user_login, name='login'),    
    path('edit_profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path("logout", views.logout_request, name= "logout"),
    
#====================== Vehicle Realated Path ========================================== 




]



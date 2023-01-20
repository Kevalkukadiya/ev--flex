from django.urls import path
from vehicle import views
from django.urls import re_path as url


urlpatterns = [
    
    path('add_vehicle/',views.add_vehicle,name='add_vehicle'),
    path('edit/<int:id>/',views.edit_vehicle,name='edit_vehicle'),
    path('retrieve',views.view_vehicle,name="view_vehicle"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete,name="delete"), 
    
    # path('vehicle_edit/',views.vehicle_edit,name='vehicle_edit'),
    # path('vehiclelist/',views.vehiclelist,name='vehiclelist'),
    # path('<int:id>',views.update_vehicle,name='update-vehicle'),
    # path('edit/<int:id>',views.edit,name="edit"),
    # path('update/<int:id>',views.update,name="update"),
    # path('edit/', views.edit_vehicle, name='edit_vehicle'),

]
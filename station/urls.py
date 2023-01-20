from django.urls import path
from . import views
from station.views import StationCreateView
from django.urls import re_path as url


urlpatterns = [

     path('view',views.view_station,name="view_station"),
     path('edit/<int:id>',views.edit_station,name="edit_station"),
     path("Add/", StationCreateView.as_view(), name="add_station"),
     url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_station,name="delete_station"), 

     
     
     # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
     # path('update/<int:id>',views.update,name="update"),
     # path('Add/', views.add_station, name='add_station'),

     # path('update/<str:pk>/', views.update_station, name='update_station'),
     # path('get/', views.view_station, name='view_station'),   
     # path('get/<int:id>/', views.view_station, name='view_station'),
     # path('delete/<str:pk>/', views.delete_station, name='delete_station'),

]
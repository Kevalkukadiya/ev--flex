from django.urls import path
from . import views
# from slot.views import SlotCreateView

urlpatterns = [
     # path("Add/", SlotCreateView.as_view(), name="create_slot"),
     path('view/', views.view_slot, name='view_slot'),
     path('edit/<int:id>/', views.edit_slot, name='edit_slot'),

     path('Add/', views.slot_create, name='create_slot'),
     # path('update/<str:pk>/', views.update_slot, name='update_slot'),
     # path('delete/<str:pk>/', views.delete_slot, name='delete_slot'),
     
]



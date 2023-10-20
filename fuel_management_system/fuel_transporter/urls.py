from django.urls import path
from .views import *

urlpatterns = [
    path('fuel_purchase_detail/', Fuel_purchased_details_View.as_view(), name = 'fuel_perchase_details'),
    path('fuel_purchase_detail/<int:id>', Fuel_purchased_details_View_by_id.as_view(), name = 'get_fuel_perchase data'),
]
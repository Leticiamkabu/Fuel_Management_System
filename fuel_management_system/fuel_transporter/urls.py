from django.urls import path
from .views import *

urlpatterns = [
    path('fuel_purchase_detail/', Fuel_purchased_details_View.as_view(), name = 'fuel_perchase_details'),

]
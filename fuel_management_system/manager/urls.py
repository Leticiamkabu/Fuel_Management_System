from django.urls import path
from .views import *

urlpatterns = [
    path('dipping/',Fuel_dipping_view.as_view(),name = 'dipping'),
    path('dipping/<int:id>',Fuel_dipping_view_by_id.as_view(),name = 'dipping_by_id'),
    path('fuel_prices/',Fuel_prices_view.as_view(),name = 'fuel_price'),
    path('fuel_prices/<int:id>',Fuel_prices_view_by_id.as_view(),name = 'fuel_price_by_id'),
]
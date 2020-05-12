from django.urls import path
from . views import Home
from cart.views import *
app_name= 'mainapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cart/',CartView,name='home1'),
     path('cart/<slug>/', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
     path('decrease-cart/<slug>', decreaseCart, name='decrease-cart'),

    

    
]
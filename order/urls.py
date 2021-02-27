from django.urls import path
from order import views

urlpatterns = [
    path('',views.user,name='index'),
    path('addtoshopcart/<int:id>',views.addtoshopcart,name='addtoshopcart'),
    path('deletefromcart/<int:id>',views.deletefromcart,name='deletefromcart'),
    path('orderproduct/',views.orderproduct,name='orderproduct'),
    path('buynow/',views.buynow,name='buynow'),
]

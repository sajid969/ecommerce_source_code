from django.contrib import admin
from order.models import *

# Register your models here.
class ShopcartAdmin(admin.ModelAdmin):
    list_display=['product','user','quantity','amount']
    list_filter=['user']
class buynowAdmin(admin.ModelAdmin):
    list_display=['product','user','quantity','amount']
    list_filter=['user']
class OrderProductLine(admin.TabularInline):
    model=OrderProduct
    readonly_fields=('user','product','price','quantity','amount',)
    can_delete=False
    extra=0
class OrderAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','phone','city','total','status']
    list_filter=['status']
    readonly_fields=('first_name','last_name','phone','city','total','status','user','address','country','ip',)
    can_delete=False
    inlines=[OrderProductLine]
class OrderProductAdmin(admin.ModelAdmin):
    list_display=['user','product','price','quantity','amount']
    list_filter=['user']

admin.site.register(Shopcart,ShopcartAdmin)
admin.site.register(buynow,buynowAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)

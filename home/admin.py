from django.contrib import admin
from home.models import *
# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display=['title','company','update_at','status']
class ContactMessagesAdmin(admin.ModelAdmin):
    list_display=['name','subject','message','status']
    readonly_fields=('name','subject','email','message','ip')


admin.site.register(ContactMessages,ContactMessagesAdmin)

admin.site.register(Setting,SettingAdmin)

from django.contrib import admin
from card_details.models import aadhar_card,pan_card
# Register your models here.

class aadhar_card_admin(admin.ModelAdmin):
    list_display=['id','number','first_name','last_name','age','mobile_number']

class pan_card_admin(admin.ModelAdmin):
    list_display=['id','number','first_name','last_name','age','mobile_number']

admin.site.register(aadhar_card,aadhar_card_admin)
admin.site.register(pan_card,pan_card_admin)

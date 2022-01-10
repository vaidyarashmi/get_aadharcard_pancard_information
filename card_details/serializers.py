from rest_framework import serializers
from card_details.models import aadhar_card,pan_card
from rest_framework.response import Response
import re


class aadhar_card_serializers(serializers.Serializer):
    def validate(self,data):
        number=data.get("aadhar_card_number")
        if re.findall(r'^[0-9]{12}$', number):
            return number
        else:
            return ValueError('Please enter valid aadhar card number')
        
    aadhar_card_number=serializers.CharField()

class pan_card_serializers(serializers.Serializer):
    def validate(self,data):
        number=data.get("pan_card_number")
        if re.findall(r'^[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}$', number):
            return number
        else:
            return ValueError('Please enter valid pan card number')
        
    pan_card_number=serializers.CharField()
    


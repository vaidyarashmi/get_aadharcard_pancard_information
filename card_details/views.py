from django.shortcuts import render
from rest_framework.views import APIView
from card_details.models import aadhar_card,pan_card
from rest_framework.response import Response
from rest_framework import status
from card_details.serializers import aadhar_card_serializers,pan_card_serializers
from card_details.mixins import mixins_reusable_code
# Create your views here.

class get_card_details(APIView,mixins_reusable_code):
    def post(self,request,*args,**kwargs):
        card_dict=['aadhar_card_number','pan_card_number']
        for key, value in request.data.items():
            if key in card_dict[0]:
                serializer=self.get_serializer(aadhar_card_serializers,request.data)
                if serializer.is_valid():
                    number=self.get_request_number(request,'aadhar_card_number')
                    aadhar_card_data=self.get_card_record(aadhar_card,number)
                    if aadhar_card_data is None:
                        return self.get_response({'msg':'aadhar card details not found'},status.HTTP_400_BAD_REQUEST)
                    return self.get_response(self.output_dict(aadhar_card_data.number,aadhar_card_data.first_name,aadhar_card_data.last_name,aadhar_card_data.age,aadhar_card_data.mobile_number),status.HTTP_200_OK)
                return self.get_response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            elif key in card_dict[1]:
                serializer=self.get_serializer(pan_card_serializers,request.data)
                if serializer.is_valid():
                    number=self.get_request_number(request,'pan_card_number')
                    pan_card_data=self.get_card_record(pan_card,number)
                    if pan_card_data is None:
                        return self.get_response({'msg':'pan card details not found'},status.HTTP_400_BAD_REQUEST)
                    return self.get_response(self.output_dict(pan_card_data.number,pan_card_data.first_name,pan_card_data.last_name,pan_card_data.age,pan_card_data.mobile_number),status.HTTP_200_OK)
                return self.get_response(serializer.errors,status.HTTP_400_BAD_REQUEST)
            else:
                return self.get_response({'msg':'Details not found, Please enter valid details'},status.HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
from rest_framework import status

class mixins_reusable_code(object):
    def get_card_record(self,table_name,number):
        try:
            card=table_name.objects.get(number=number)
        except:
            card=None
        return card
    def get_response(self,json_data,status):
        return Response(json_data,status=status)
    def output_dict(self,number,first_name,last_name,age,mobile_number):
        card_details={
                        "number":number,
                        "first_name":first_name,
                        "last_name":last_name,
                        "age":age,
                        "mobile_number":mobile_number,
                        }
        return card_details
    def get_request_number(self,request,data):
        number=request.data.get(data)
        return number
    def get_serializer(self,card_serializers,request):
        serializer=card_serializers(data=request)
        return serializer
            

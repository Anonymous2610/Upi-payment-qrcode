from django.shortcuts import render
import re
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import FileResponse
# Create your views here.
import qrcode
import png

# Generate the QR code using the UPI string
def isValidUpi(str):
    # Regex to check valid UPI ID
    regex = "^[a-zA-Z0-9.-]{2, 256}@[a-zA-Z][a-zA-Z]{2, 64}$"
    # Compile the ReGex
    p = re.compile(regex)
    # If the string is empty
    # return false
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False


#view for generating the QR code
class UPI(APIView):
    def post(self,request):
        data=request.data
        print(data)
        upi_id=data["id"]
        amount=1
        if isValidUpi(upi_id):
            return HttpResponse("Invalid UPI string")

        upistring = f"upi://pay?pa={upi_id}&am={amount}&mc=0000&mode=02&purpose=00&orgid=159761"
        qr_code = qrcode.make(upistring)
        qr_code.save("upi.png")
        img = open('upi.png', 'rb')
        response = FileResponse(img)
        return response
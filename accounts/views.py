from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# Create your views here.

# Registration

class Register(APIView):
    def post(self,request):
        try:
            print(request.data,'dataaaaa')
            return Response({'message':'checking'})
        except Exception as e:
            print(e)
            return Response({'error':e})

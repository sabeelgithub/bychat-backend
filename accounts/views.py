from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer


# Create your views here.

# Registration

class Register(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({'error':serializer.errors,'message':'something for serializer','status':500})
            serializer.save()           
            return Response({'message':'Registration Successfull,you can Login','status':201})
        except Exception as e:
            return Response({'error':e})

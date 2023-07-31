from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import CustomUser
from .serializers import UsersListSerializer

# Create your views here.


class Users(APIView):
    # get users list
    def get(self,request):
        try:
            print('reached')
            users = CustomUser.objects.filter(is_superuser=False)
            print(users,'users')
            if users:
              serializer = UsersListSerializer(users,many=True)
              print(serializer)
              return Response({'users':serializer.data,'status':200})
            return Response({'message':'No users','status':404})
        except Exception as e:
            print(e)
            return Response({'error':e})
    # block / unblock users
    def patch(self,request):
        try:
            user = CustomUser.objects.get(id=request.data['id'])
            if request.data['status'] == False:
                user.is_block = True
                user.save()
                return Response({'message':f'{user} is Blocked','status':200})
            elif request.data['status'] == True:
                user.is_block = False
                user.save()
                return Response({'message':f'{user} is Unblocked','status':200})
        except Exception as e:
            return Response({'error':e})



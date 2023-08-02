from rest_framework import serializers
from .models import *

# for registration
class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username','email','mobile','password','specification']

    def validate(self,data):
        if data['username']:
            for i in data['username']:
                if i.isdigit():
                    raise serializers.ValidationError({'error':'name cannot contain numbers'})
        if data['mobile']:
            num = str(data['mobile'])
            if len(num) > 10 :
                raise serializers.ValidationError({'error':'mobile number not more than 10'})
        
        return data
    
    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'],mobile=validated_data['mobile'],username=validated_data['username'])
        user.specification = validated_data['specification']
        user.set_password(validated_data['password'])
        user.save()
        return user
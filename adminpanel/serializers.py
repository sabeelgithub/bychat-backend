from rest_framework import serializers
from accounts.models import CustomUser

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','specification','email','mobile','is_block','id']

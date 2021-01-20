from rest_framework.serializers import ModelSerializer
from api.models import User, SMS


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        depth = 2
        fields = '__all__'


class SMSSerializer(ModelSerializer):
    
    class Meta:
        model = SMS
        depth = 1
        fields = '__all__'

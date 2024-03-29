from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from .models import participator

class participatorSrializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.participator
        fields = '__all__'

class RegistrationSrializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    image = serializers.ImageField()
    mobile_no = serializers.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email','mobile_no', 'image', 'password', 'confirm_password',]

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        image = self.validated_data.get('image')
        mobile_no = self.validated_data.get('mobile_no')



        if password != password2:
            raise serializers.ValidationError({'error': "password Doesn't matched"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        account.set_password(password)
        account.is_active = False
        account.save()
        participator.objects.create(
            user = account,
            image = image,
            mobile_no = mobile_no,
            score =0,
            complete=0,
        )
        return account
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required = True)      
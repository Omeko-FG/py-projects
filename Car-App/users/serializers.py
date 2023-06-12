from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer


class UserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )


    password = serializers.CharField(
        required = False,
        write_only = True,
    )
    
    class Meta:
        model = User
        exclude=[]

    def validate(self, attrs):
        if attrs.get('password', False):
            from django.contrib.auth.password_validation import validate_password
            from django.contrib.auth.hashers import make_password
            password = attrs['password']
            validate_password(password)
            attrs.update({'password': make_password(password)})
        return super().validate(attrs)




# class CustomTokenSerializer(TokenSerializer):

#     user = UserSerializer(read_only=True)

#     class Meta(TokenSerializer.Meta):
#         fields = (
#             'key',
#             'user',
#             )


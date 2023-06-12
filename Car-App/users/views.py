
from rest_framework.generics import ( CreateAPIView,
                                     RetrieveUpdateAPIView)
from django.contrib.auth.models import User
from .serializers import (User,
                          UserSerializer)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# class RegisterView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
        
#         user = serializer.save()
#         data = serializer.data
#         if Token.objects.filter(user=user).exists():
#             token = Token.objects.get(user=user)
#             data['token'] = token.key
#         else:
#             data['token'] = 'No token created for this user!!!'

#         headers = self.get_success_headers(serializer.data)
#         return Response(data, status=status.HTTP_201_CREATED, headers=headers)


# class ProfileUpdateView(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = (IsAuthenticated, IsOwnerOrStaff)


# @api_view(['POST'])
# def logout(request):
#     request.user.auth_token.delete()
#     data = {
#         'message':'Logged out succesfully!'
#     }
#     return Response(data, status=status.HTTP_200_OK)


from .serializers import (
    User, UserSerializer
)


#-----------------------------------------
#           USERCREATEVİEW
#----------------------------------------
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

class UserCreateView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response
        from rest_framework.authtoken.models import Token
        # Defaults:
        serializer.validated_data['is_superuser'] = False
        serializer.validated_data['is_staff'] = False
        serializer.validated_data['is_active'] = True
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # <--- User.save() & Token.create() --->
        user = serializer.save()
        data = serializer.data
        token = Token.objects.create(user=user)
        data['key'] = token.key
        # </--->
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


# -------------------------------
# UserView
# -------------------------------
from rest_framework.viewsets import ModelViewSet

class UserView(ModelViewSet):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer
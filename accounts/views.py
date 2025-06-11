from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from .serializers import CustomUserSerializer, PasswordChangeSerializer, ShowProfile
from .models import CustomUser

@swagger_auto_schema(method='POST', request_body=CustomUserSerializer, operation_id='Register', operation_summary='Register new user if not logged in or don\'t have an account')
@api_view(['POST'])
def accounts_register(request):
    if request.user.is_authenticated:return Response({'message':'you\'ve already logged in!'})
    serializer = CustomUserSerializer
    model = CustomUser
    data = serializer(data=request.data)
    if data.is_valid():data.save();return Response(data.data)
    return Response(data.errors)

@swagger_auto_schema(method='GET', operation_id='Show profile')
@api_view()
def accounts_show_profile(request):
    serializer = ShowProfile
    user = request.user
    if user.is_authenticated:return Response(serializer(user).data)
    return Response({'message':'you are not logged in!'})

@swagger_auto_schema(method='POST', request_body=PasswordChangeSerializer, operation_id='Change password', operation_summary='Used to change password')
@api_view(['POST'])
def accounts_password_change(request):
    user = request.user
    if user.is_authenticated:
        if not user.check_password(request.data.get('old_password')):return Response({'message':'The password is incorrect'})
        user.set_password(request.data.get('new_password'))
        user.save()
        return Response({'message':'Successfully changed!'})
    return Response({'message':'you are not logged in!'})

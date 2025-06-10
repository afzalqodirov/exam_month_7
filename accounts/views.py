from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from .serializers import CustomUserSerializer
from .models import CustomUser

@swagger_auto_schema(method='POST', request_body=CustomUserSerializer)
@api_view(['POST'])
def accounts_register(request):
    if request.user.is_authenticated:return Response({'message':'you\'ve already logged in!'})
    serializer = CustomUserSerializer
    model = CustomUser
    data = serializer(data=request.data)
    if data.is_valid():data.save();return Response(data.data)
    return Response(data.errors)

@api_view()
def accounts_show_profile(request):
    serializer = CustomUserSerializer
    user = request.user
    if user.is_authenticated:return Response(serializer(user).data)
    return Response({'message':'you are not logged in!'})

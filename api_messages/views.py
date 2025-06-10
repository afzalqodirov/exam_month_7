from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

# my imports
from .serializers import MessagesSerializer

@swagger_auto_schema(method='POST', request_body=MessagesSerializer, operation_id='Messages', operation_summary='send message')
@api_view(['POST'])
def send_message(request):
    if not request.user.is_authenticated:return Response({'message':'You are not logged in!'})
    serializer = MessagesSerializer(data=request.data, context={'request':request})
    if serializer.is_valid():serializer.save();return Response(serializer.data)
    return Response(serializer.errors)

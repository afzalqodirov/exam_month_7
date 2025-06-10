from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

#my imports
from .serializers import PapersSerializer
from .models import PapersModel

@swagger_auto_schema(method='POST', request_body=PapersSerializer, operation_id='Post Paper')
@api_view(['POST'])
def post_paper(request):
    if not request.user.is_authenticated:return Response({'message':'You are not logged in!'})
    serializer = PapersSerializer(data=request.data, context={'user':request.user})
    if serializer.is_valid():serializer.save();return Response(serializer.data)
    return Response(serializer.errors)

@swagger_auto_schema(method='GET', operation_id='Get Papers')
@api_view()
def get_papers(request):
    objs = PapersModel.objects.filter(is_reviewed=True)
    serializer = PapersSerializer
    return Response(serializer(objs, many=True).data)

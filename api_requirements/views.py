from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from .serializers import RequirementsSerializer
from .models import RequirementsModel
from django.shortcuts import get_object_or_404

@swagger_auto_schema(method='GET', manual_parameters = [openapi.Parameter('id', 'query', 'search by id or by default id = 1', False, type='integer')])
@api_view()
def get_requirements(request):
    id = request.GET.get('id')
    if not id:id = 1
    model = RequirementsModel
    serializer = RequirementsSerializer
    obj = get_object_or_404(model, pk=id)

    # try except is not used because there's a hope that frontend uses the "right" id's
    # othervise it slows the server
    return Response(serializer(obj).data, status=200)

@swagger_auto_schema(method='POST', request_body=RequirementsSerializer)
@api_view(['POST'])
def temp(request):
    serializer = RequirementsSerializer(data=request.data)
    if serializer.is_valid():serializer.save();return Response(serializer.data)
    return Response(serializer.errors)

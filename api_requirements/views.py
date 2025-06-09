from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from .serializers import RequirementsSerializer
from .models import RequirementsModel
from django.shortcuts import get_object_or_404

@swagger_auto_schema(method='GET', manual_parameters = [openapi.Parameter('id', 'query', 'search by id or by default id=1', False, type='integer')])
@api_view()
def get_requirements(request):
    id = request.GET.get('id')
    if not id:id = 1
    #return Response(RequirementsSerializer(get_object_or_404(RequirementsModel, pk=id)).data, status=200)
    return Response(RequirementsSerializer(RequirementsModel.objects.all(), many=True).data)

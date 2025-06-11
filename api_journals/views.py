from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

# my imports
from .serializers import JournalsSerializer_UZ, JournalsSerializer_RU, JournalsSerializer_EN, JournalsSerializerList_UZ, JournalsSerializerList_RU, JournalsSerializerList_EN
from .models import JournalsModel_UZ, JournalsModel_RU, JournalsModel_EN

@api_view()
def get_journals(request):
    if 'ru' in request.path:model = JournalsModel_RU;serializer = JournalsSerializerList_RU
    elif 'en' in request.path:model = JournalsModel_EN;serializer = JournalsSerializerList_EN
    else:model = JournalsModel_UZ; serializer = JournalsSerializerList_UZ
    objs = model.objects.all()
    return Response(serializer(objs, many=True).data)

@swagger_auto_schema(method='GET', manual_parameters = [openapi.Parameter('id', 'query', type='integer')])
@api_view()
def retrieve_journal(request):
    if 'ru' in request.path:model = JournalsModel_RU;serializer = JournalsSerializer_RU
    elif 'en' in request.path:model = JournalsModel_EN;serializer = JournalsSerializer_EN
    else:model = JournalsModel_UZ; serializer = JournalsSerializer_UZ
    obj = get_object_or_404(model, pk=request.GET.get('id'))
    return Response(serializer(obj).data)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404
from django.db.models import Q

#my imports
from .serializers import PapersSerializer_UZ, PapersSerializer_RU, PapersSerializer_EN
from .models import PapersModel_UZ, PapersModel_RU, PapersModel_EN

@swagger_auto_schema(method='POST', request_body=PapersSerializer_UZ)
@api_view(['POST'])
def post_paper(request):
    if not request.user.is_authenticated:return Response({'message':'You are not logged in!'})
    if 'ru' in request.path:serializer = PapersSerializer_RU
    elif 'en' in request.path:serializer = PapersSerializer_EN
    else: serializer=PapersSerializer_UZ
    data = serializer(data=request.data, context={'user':request.user})
    if data.is_valid():data.save();return Response(data.data)
    return Response(data.errors)

@swagger_auto_schema(method="GET", manual_parameters=[openapi.Parameter('title', 'query', type='string'), openapi.Parameter('author', 'query', type='string'), openapi.Parameter('keywords', 'query', type='string'), openapi.Parameter('references', 'query', type='string')])
@api_view()
def get_papers(request):
    if 'ru' in request.path:model = PapersModel_RU;serializer = PapersSerializer_RU
    elif 'en' in request.path:model = PapersModel_EN;serializer = PapersSerializer_EN
    else: model = PapersModel_UZ;serializer = PapersSerializer_UZ
    objs = model.objects.filter(is_reviewed=True)
    title = request.GET.get('title')
    author = request.GET.get('author')
    keywords = request.GET.get('keywords')
    references = request.GET.get('references')
    if title:objs = objs.filter(title__istartswith=title)
    if author:objs = objs.filter(author__username__icontains=author)
    if keywords:objs = objs.filter(article__icontains=keywords)
    if references:objs = objs.filter(reference=references)
    return Response(serializer(objs, many=True).data)

@swagger_auto_schema(method='GET', operation_summary='Retrieves paper by id, no default', manual_parameters=[openapi.Parameter('id', 'query', type='integer')])
@api_view()
def retrieve_paper(request):
    if not request.user.is_authenticated:return Response({'message':'You are not logged in!'})
    if 'ru' in request.path:model = PapersModel_RU;serializer = PapersSerializer_RU
    elif 'en' in request.path:model = PapersModel_EN;serializer = PapersSerializer_EN
    else: model = PapersModel_UZ;serializer = PapersSerializer_UZ
    obj = get_object_or_404(model, pk=request.GET.get('id'))
    return Response(serializer(obj).data)

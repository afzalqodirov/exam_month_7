from rest_framework.response import Response
from rest_framework.decorators import api_view

# my imports
from .serializers import FAQSerializer
from .models import FAQModel


@api_view()
def show_faq(request):
    serializer = FAQSerializer
    model = FAQModel
    obj = model.objects.all()
    return Response(serializer(obj, many=True).data, status=200)


# temp
from drf_yasg.utils import swagger_auto_schema
@swagger_auto_schema(method = 'POST', request_body = FAQSerializer)
@api_view(['POST'])
def tempp(request):
    serializer = FAQSerializer
    data = serializer(data=request.data)
    if data.is_valid():data.save();return Response(data.data)
    return Response(data.errors)

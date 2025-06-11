from rest_framework.response import Response
from rest_framework.decorators import api_view

# my imports
from api_journals.serializers import JournalsSerializer_UZ, JournalsSerializer_RU, JournalsSerializer_EN, JournalsSerializerList_UZ, JournalsSerializerList_RU, JournalsSerializerList_EN
from api_journals.models import JournalsModel_UZ, JournalsModel_RU, JournalsModel_EN
from api_papers.serializers import PapersSerializer_UZ, PapersSerializer_RU, PapersSerializer_EN
from api_papers.models import PapersModel_UZ, PapersModel_RU, PapersModel_EN

@api_view()
def get_main(request):
    if 'ru' in request.path:journal=JournalsModel_RU;journal_serializer=JournalsSerializer_RU;paper=PapersModel_RU;papers_serializer=PapersSerializer_RU
    elif 'en' in request.path:journal=JournalsModel_EN;journal_serializer=JournalsSerializer_EN;paper=PapersModel_RU;papers_serializer=PapersSerializer_RU
    else:journal=JournalsModel_UZ;journal_serializer=JournalsSerializer_UZ;paper=PapersModel_RU;papers_serializer=PapersSerializer_RU
    journals_obj = journal.objects.all().order_by('-created_at').first()
    papers_objs_last = paper.objects.all().order_by('created_at')[:4]
    papers_objs_most_viewed = paper.objects.all().order_by('views_count')[:6]
    return Response({
        "Last Edition":journal_serializer(journals_obj).data,
        "Last Papers":papers_serializer(papers_objs_last, many=True).data,
        "Most read Paper":papers_serializer(papers_objs_most_viewed, many=True).data
        })

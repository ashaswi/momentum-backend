from rest_framework import viewsets
from mysite.models import Survey
from mysite.serializers.survery_serializer import SurveySerializer



class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
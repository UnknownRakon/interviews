from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
import django_filters.rest_framework
from api.models import Employer, Finder, Vacancy, Interview
from api.serializers import EmployerSerializer, FinderSerializer, VacancySerializer, InterviewSerializer


class EmployerViewSet(ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class FinderViewSet(ModelViewSet):
    queryset = Finder.objects.all()
    serializer_class = FinderSerializer


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class InterviewViewSet(ModelViewSet):
    queryset = Interview.objects.filter(Q(status='PLANNED') | Q(status='PROCESSING'))
    serializer_class = InterviewSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, ]
    filterset_fields = ['employer', 'finder', 'vacancy']

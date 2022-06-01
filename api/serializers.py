from rest_framework.serializers import ModelSerializer
from api.models import Employer, Finder, Vacancy, Interview


class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class FinderSerializer(ModelSerializer):
    class Meta:
        model = Finder
        fields = '__all__'


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class InterviewSerializer(ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'



from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from api.models import Employer, Finder, Vacancy, Interview

@admin.register(Employer)
class EmployerAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True

@admin.register(Finder)
class FinderAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True

@admin.register(Vacancy)
class VacancyAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True

@admin.register(Interview)
class InterviewAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True

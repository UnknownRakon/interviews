from rest_framework.routers import DefaultRouter
from authentication.views import UserViewSet
from api.views import EmployerViewSet, FinderViewSet, VacancyViewSet, InterviewViewSet


router = DefaultRouter()
router.register('auth', UserViewSet)
router.register('employer', EmployerViewSet)
router.register('finder', FinderViewSet)
router.register('vacancy', VacancyViewSet)
router.register('interview', InterviewViewSet)

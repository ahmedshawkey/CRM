from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, StageViewSet

router = DefaultRouter()
router.register(r'leads', LeadViewSet)
router.register(r'stages', StageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

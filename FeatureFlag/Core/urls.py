from django.urls import path, include
from rest_framework import routers

from .views import FeatureViewSet, get_rule_names

router = routers.DefaultRouter()
router.register(
    'feature', FeatureViewSet
)

urlpatterns = [
    path('', include(router.urls)),
    path('rule/', get_rule_names)
]

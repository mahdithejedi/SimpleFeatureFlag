from django.urls import path, include
from rest_framework import routers

from .views import FeatureViewSet, UserViewSet, get_rule_names

router = routers.DefaultRouter()
router.register(
    'feature', FeatureViewSet
)
router.register(
    'user', UserViewSet
)

urlpatterns = [
    path('', include(router.urls)),
    path('rule/', get_rule_names)
]

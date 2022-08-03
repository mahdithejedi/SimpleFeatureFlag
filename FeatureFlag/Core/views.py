from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Feature
from .serializers import FeatureSerializer


class FeatureViewSet(ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


@api_view(['GET'])
def get_rule_names(request, *args, **kwargs):
    return Response(
        {
            'rules': Feature.RuleChoices.names
        },
        status=HTTP_200_OK
    )
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Feature, User
from .serializers import FeatureSerializer, UserSerializer
from .Rules.manager import RuleManager


class FeatureViewSet(ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        manager = RuleManager(
            serializer.data['user_id'],
            serializer.data['version']
        )
        return Response(
            manager.get_features(),
            status=HTTP_200_OK
        )


@api_view(['GET'])
def get_rule_names(request, *args, **kwargs):
    return Response(
        {
            'rules': Feature.RuleChoices.names
        },
        status=HTTP_200_OK
    )
from ..models import Feature, User
from django.db.models import Q


class RuleManager:
    def __init__(self, user_id, version):
        self._feature = Feature
        self._user = User
        self._user_id = user_id
        self._version = version

    def get_features(self):
        Q_queryset = Q()
        for cls in self._user.get_rule_classes():
            rule_cls = cls(self._feature, self._user, self._user_id, self._version)
            if _q := rule_cls.get_features():
                Q_queryset |= _q
        return self.__response(
            Q_queryset
        )

    def __response(self, Q_queryset):
        res = Feature.objects.filter(Q_queryset).values_list('name', flat=True)
        return {
            'functions': res
        }

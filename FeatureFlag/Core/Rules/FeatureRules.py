from abc import ABC
from django.db.models import Q


class _BaseRule(ABC):
    def __init__(self, feature, user, user_id, version):
        self._feature = feature
        self._user = user
        self._user_id = user_id
        self._version = version

    def get_features(self):
        raise NotImplementedError(
            "You should Implement this feature"
        )


class GlobalRule(_BaseRule):
    def get_features(self):
        return Q(rule=self._feature.RuleChoices.Global)


class PartialRule(_BaseRule):
    pass


class MinimumRule(_BaseRule):
    def get_features(self):
        major_version, minor_version, patches = self._version.split('.')
        return \
            Q(Q(major_version__gte=major_version) |
             Q(major_version=major_version, minor_version__gte=minor_version) |
             Q(major_version=major_version, minor_version=minor_version, patches__gte=patches))


class MinimumPartialRule(_BaseRule):
    pass

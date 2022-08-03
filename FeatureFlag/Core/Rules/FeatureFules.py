from abc import ABC

from ..models import Feature


class _BaseRule(ABC):
    def __init__(self, queryset, user_id, version):
        self._queryset = queryset
        self._user_id = user_id
        self._version = version

    def get_features(self):
        raise NotImplementedError(
            "You should Implement this feature"
        )


class GlobalRule(_BaseRule):
    def get_features(self):
        return Feature.objects.filter(rule=Feature.RuleChoices.Global).values_list('name')


class PartialRule(_BaseRule):
    pass


class MinimumRule(_BaseRule):
    def get_features(self):
        major_version, minor_version, patches = self._version.split('.')
        return Feature.objects.filter(
            major_version__gte=major_version,
            monir_version__gte=minor_version,
            pathces__gte=patches
        ).values_list('name')


class MinimumPartialRule(_BaseRule):
    pass

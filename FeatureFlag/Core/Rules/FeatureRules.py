from abc import ABC
from functools import partial
from time import mktime
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
    @staticmethod
    def __get_remainder_hash(user, user_id):
        user, _ = user.objects.get_or_create(user_id=user_id)
        unix_time = mktime(user.created_at.timetuple())
        return int(hash(
            f'{user_id}#{unix_time}'
        ) % 100)

    def get_features(self):
        partial_percent = self.__get_remainder_hash(self._user, self._user_id)
        return Q(
            percent__gte=partial_percent, rule=self._feature.RuleChoices.Partial
        )


class MinimumRule(_BaseRule):
    def get_features(self):
        major_version, minor_version, patches = self._version.split('.')
        Q_rule = partial(
            rule=self._feature.RuleChoices.Partial
        )
        return \
            Q(Q_rule(major_version__gt=major_version) |
           Q_rule(major_version=major_version, minor_version__gt=minor_version) |
           Q_rule(major_version=major_version, minor_version=minor_version, patches__gte=patches))


class MinimumPartialRule(_BaseRule):
    def get_features(self):
        Q(rule=self._feature.RuleChoices.MinimumPartial) & Q(
            MinimumRule.get_features(self) &
            PartialRule.get_features(self)
        )

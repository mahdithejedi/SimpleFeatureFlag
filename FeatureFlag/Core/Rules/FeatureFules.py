from abc import ABC


class _BaseRule(ABC):
    pass


class GlobalRule(_BaseRule):
    pass


class PartialRule(_BaseRule):
    pass


class MinimumRule(_BaseRule):
    pass


class MinimumPartialRule(_BaseRule):
    pass

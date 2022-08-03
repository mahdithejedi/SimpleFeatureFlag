class RuleManager:
    def __init__(self,model, queryset, user_id, version):
        self._model = model
        self._queryset = queryset
        self._user_id = user_id
        self._version = version

    def get_features(self):
        _functions = []
        for cls in self._model.get_rule_classes():
            rule_cls = cls(self._queryset, self._user_id, self._version)
            _functions.extend(
                rule_cls.get_features()
            )
        return self.__response(
            _functions
        )

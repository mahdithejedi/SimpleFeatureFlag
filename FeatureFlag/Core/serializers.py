from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import Feature, User


class FeatureSerializer(serializers.ModelSerializer):
    version = serializers.RegexField(
        # todo change regex, don't support 12.14.15
        r'(\d\.){2}\d',
        allow_null=True,
        required=False,
        error_messages={
            'invalid': _("version should be in the format of Number.Number.Number")
        }
    )

    class Meta:
        model = Feature
        fields = (
            'pk', 'rule', 'name',
            'version', 'percent'
        )

    def validate(self, attrs):
        rule = attrs['rule']
        if rule == Feature.RuleChoices.Minimum and not attrs.get('version'):
            raise serializers.ValidationError(
                f"if you specify '{Feature.RuleChoices.Minimum}' you should set 'version' to"
            )
        elif rule == Feature.RuleChoices.Minimum:
            attrs['major_version'], attrs['minor_version'], attrs['patches'] = attrs.pop('version').split('.')
        if rule == Feature.RuleChoices.Partial and not attrs.get('percent'):
            raise serializers.ValidationError(
                f"if you specify '{Feature.RuleChoices.Partial}' you should set 'percent' to"
            )
        if rule == Feature.RuleChoices.MinimumPartial and (
            not attrs.get('percent') or not attrs.get('version')
        ):
            raise serializers.ValidationError(
                f"if you specify '{Feature.RuleChoices.MinimumPartial} you should set both 'percent' and 'version' to"
            )
        elif rule == Feature.RuleChoices.MinimumPartial:
            version = attrs.pop('version')
            attrs['major_version'], attrs['minor_version'], attrs['patches'] = version.split('.')

        return super().validate(attrs)

    def to_representation(self, instance):
        instance.version = '%s.%s.%s' % (
            instance.major_version or '',
            instance.minor_version or '',
            instance.patches or ''
        )
        return super().to_representation(instance)


class UserFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = (
            'name'
        )


class UserSerializer(serializers.ModelSerializer):
    version = serializers.RegexField(
        r'(\d\.){2}\d',
        allow_null=True,
        required=False,
        error_messages={
            'invalid': _("version should be in the format of Number.Number.Number")
        }
    )
    user_id = serializers.IntegerField()

    class Meta:
        model = User
        fields = (
            'user_id', 'version'
        )
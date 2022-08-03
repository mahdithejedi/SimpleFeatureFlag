from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import Feature


class FeatureSerializer(serializers.ModelSerializer):
    version = serializers.RegexField(
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
            'version'
        )

    def validate(self, attrs):
        if version := attrs.pop('version', None):
            attrs['major_version'], attrs['minor_version'], attrs['patches'] = version.split('.')
        return super().validate(attrs)

    def to_representation(self, instance):
        instance.version = '%s.%s.%s' % (
            instance.major_version or '',
            instance.minor_version or '',
            instance.patches or ''
        )
        return super().to_representation(instance)

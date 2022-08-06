from django.db import models
from datetime import datetime

from .Rules.FeatureRules import (
    GlobalRule, PartialRule,
    MinimumRule, MinimumPartialRule
)


class TimestampedModel(models.Model):
    # A primary auto increment key.
    # id = models.AutoField(primary_key=True)

    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True

        ordering = ['-created_at', '-updated_at']


class Feature(TimestampedModel):
    _rules_classes = {
        'Global': GlobalRule,
        'Partial': PartialRule,
        'Minimum': MinimumRule,
        'MinimumPartial': MinimumPartialRule
    }

    class RuleChoices(models.TextChoices):
        Global = 'Global'
        Partial = 'Partial'
        Minimum = 'Minimum'
        MinimumPartial = 'MinimumPartial'

    rule = models.CharField(
        max_length=120,
        choices=RuleChoices.choices,
        default=RuleChoices.Global
    )
    percent = models.PositiveSmallIntegerField(
        null=True, blank=True
    )
    name = models.CharField(
        max_length=250, unique=True
    )
    major_version = models.PositiveSmallIntegerField(
        null=True, blank=True, db_index=True
    )
    minor_version = models.PositiveSmallIntegerField(
        null=True, blank=True
    )
    patches = models.PositiveSmallIntegerField(
        null=True, blank=True
    )

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    'major_version', 'minor_version'
                ]
            ),
            models.Index(
                fields=[
                    'major_version', 'minor_version', 'patches'
                ]
            )
        ]

    @property
    def rule_class(self):
        return self.all_rule_cls[
            self.name
        ]

    @staticmethod
    def all_rule_cls():
        return Feature._rules_classes


class User(TimestampedModel):
    # although we have pk for User
    # we should specify user_id which interact with API Gateway
    user_id = models.IntegerField(null=False, blank=False,
                                  db_index=True, unique=True)

    @staticmethod
    def get_rule_classes():
        return Feature.all_rule_cls().values()

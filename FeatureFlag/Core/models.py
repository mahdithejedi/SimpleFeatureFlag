from datetime import datetime
from django.db import models
from .Rules.FeatureFules import (
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


class Functions(TimestampedModel):
    name = models.CharField(
        max_length=250
    )
    version = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )


class Rule(TimestampedModel):
    class RuleChoices(models.TextChoices):
        Global = GlobalRule
        Partial = PartialRule
        Minimum = MinimumRule
        MinimumPartial = MinimumPartialRule

    name = models.CharField(
        max_length=120,
        choices=RuleChoices.choices,
        default=RuleChoices.Global
    )
    Function = models.ForeignKey(
        to=Functions,
        null=True,
        on_delete=models.SET_NULL,
        related_name='rule'
    )


class User(TimestampedModel):
    # although we have pk for User
    # we should specify user_id which interact with API Gateway
    user_id = models.IntegerField(null=False, blank=False)
    rule = models.ForeignKey(
        to=Rule,
        on_delete=models.CASCADE
    )

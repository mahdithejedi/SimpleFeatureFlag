from django.db import models
from .Rules.FeatureFules import (
    GlobalRule, PartialRule,
    MinimumRule, MinimumPartialRule
)


class Functions(models.Model):
    name = models.CharField(
        max_length=250
    )


class User(models.Model):
    class RuleChoices(models.TextChoices):
        Global = GlobalRule
        Partial = PartialRule
        Minimum = MinimumRule
        MinimumPartial = MinimumPartialRule

    # although we have pk for User
    # we should specify user_id which interact with API Gateway
    user_id = models.IntegerField(null=False, blank=False)
    rule = models.IntegerField(
        choices=RuleChoices.choices,
        default=RuleChoices.Global,
        max_length=100
    )
    functions = models.ForeignKey(
        to=Functions,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_function',
        related_query_name='user_function_query'
    )

# Generated by Django 4.0.6 on 2022-08-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_remove_user_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='percent',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]

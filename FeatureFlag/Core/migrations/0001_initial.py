# Generated by Django 4.0.6 on 2022-08-03 09:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('rule', models.CharField(choices=[('Global', 'Global'), ('Partial', 'Partial'), ('Minimum', 'Minimum'), ('MinimumPartial', 'Minimumpartial')], default='Global', max_length=120)),
                ('name', models.CharField(max_length=250)),
                ('major_version', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('minor_version', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('patches', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('user_id', models.IntegerField(db_index=True, unique=True)),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_function', to='Core.feature')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['major_version', 'minor_version'], name='Core_featur_major_v_4c2f67_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['major_version', 'minor_version', 'patches'], name='Core_featur_major_v_674f8e_idx'),
        ),
    ]

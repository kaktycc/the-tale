# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-01-04 18:08
from __future__ import unicode_literals

import json

from django.db import migrations


def reset_actions_and_quests(apps, schema_editor):
    for hero in apps.get_model("heroes", "Hero").objects.all().iterator():

        actions = json.loads(hero.actions)

        actions['actions'] = [actions['actions'][0]]

        hero.actions = json.dumps(actions, ensure_ascii=False)

        hero.data['quests']['quests'] = []

        hero.save()


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0026_auto_20190104_1720'),
    ]

    operations = [
        migrations.RunPython(reset_actions_and_quests)
    ]

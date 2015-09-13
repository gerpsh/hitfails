# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20150715_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childcomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='user',
        ),
        migrations.RemoveField(
            model_name='parentcomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]

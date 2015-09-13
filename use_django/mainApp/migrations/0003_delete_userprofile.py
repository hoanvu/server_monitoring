# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20150912_1728'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

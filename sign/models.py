# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Testcase(models.Model):
    name=models.CharField(max_length=100)
    baseurl=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    args=models.CharField(max_length=1000)
    method=models.CharField(max_length=10)
    create_time=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint:disable=E1101

from django.contrib.auth.models import User
from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class UserAttribute(models.Model):
    user = models.OneToOneField(User)
    attribute = models.ManyToManyField(Attribute)

    def __unicode__(self):
        return ", ".join([a.name for a in self.attribute.all()])

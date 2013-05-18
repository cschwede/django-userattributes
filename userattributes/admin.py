#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint:disable=E1101

from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from django.conf import settings

from userattributes.models import Attribute, UserAttribute


def attribute_list_filter(_id):
    class AttributeListFilter(SimpleListFilter):
        title = _('Attribute')
        parameter_name = 'attribute' + str(_id)

        def lookups(self, request, model_admin):
            attrs = Attribute.objects.all()
            return [(a.id, a.name) for a in attrs]

        def queryset(self, request, queryset):
            if self.value():
                return queryset.filter(
                    userattribute__attribute__id=self.value())
            return queryset
    return AttributeListFilter


class UserAttributeInline(admin.StackedInline):
    model = UserAttribute
    filter_horizontal = ('attribute',)
    can_delete = False


class UserAdminWithAttributes(UserAdmin):
    count = 2
    if hasattr(settings, 'USERATTRIBUTE_FILTER_COUNT'):
        count = settings.USERATTRIBUTE_FILTER_COUNT
    list_filter = list(UserAdmin.list_filter)
    for _id in range(count):
        list_filter.append(attribute_list_filter(_id))
    inlines = list(UserAdmin.inlines)
    inlines.append(UserAttributeInline)


admin.site.register(Attribute)

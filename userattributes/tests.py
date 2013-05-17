""" Tests for userattribute """
#pylint:disable=E1101, C0111, R0904, C0301
from django.test import TestCase
from django.test.utils import setup_test_environment
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User

from userattributes.models import UserAttribute, Attribute
from userattributes.admin import attribute_list_filter, UserAdminWithAttributes

setup_test_environment()


class ModelTests(TestCase):
    """ Tests for userattribute """

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.attribute = Attribute.objects.create(name='nice guy')
        self.attribute2 = Attribute.objects.create(name='bad guy')
        self.userattribute = UserAttribute.objects.create(user=self.user)
        self.userattribute.attribute.add(self.attribute)
        self.site = AdminSite()
        self.request = None

    def test_unicode(self):
        self.assertEqual(str(self.attribute), 'nice guy')
        self.assertEqual(str(self.userattribute), 'nice guy')

    def test_list_filter(self):
        user_admin = UserAdminWithAttributes(self.user, self.site)
        tmp = attribute_list_filter(0)
        parameter_names = []
        for alf in user_admin.list_filter:
            if not isinstance(alf, str):
                parameter_names.append(alf.__dict__['parameter_name'])
        self.assertEqual(set(parameter_names),
                         set(['attribute0', 'attribute1', 'attribute2']))

        alf = tmp(self.request, {}, self.user, user_admin)
        self.assertEqual(set(alf.lookups(self.request, user_admin)),
                        (set([(1, u'nice guy'), (2, u'bad guy')])))

        users = User.objects.all()
        self.assertEqual(alf.queryset(self.request, users), users)
        alf = tmp(self.request, {'attribute0': '1'}, self.user, user_admin)
        self.assertEqual(set(alf.queryset(self.request, users)),
                         set(users))

        alf = tmp(self.request, {'attribute0': '2'}, self.user, user_admin)
        self.assertEqual(set(alf.queryset(self.request, users)),
                         set([]))

from django.db import models
import random
import string

from django.contrib.sessions.models import Session
from django.contrib.sites.models import Site
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group

Session._meta.db_table = 'sessions'
Site._meta.db_table = 'sites'
LogEntry._meta.db_table = 'admin_log'
ContentType._meta.db_table = 'content_types'
Permission._meta.db_table = 'auth_perm'
Group._meta.db_table = 'auth_group'


def generate_category_id():
    id = ''.join(random.sample(string.lowercase + string.digits, 32))
    if not Category.objects.filter(pk=id).exists():
        return 'category-' + id


def generate_component_id():
    id = ''.join(random.sample(string.lowercase + string.digits, 32))
    if not Component.objects.filter(pk=id).exists():
        return 'component-' + id


class Category(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=generate_category_id, editable=False)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)

    class Meta:
        db_table = 'categories'
        ordering = ['name',]

    def __unicode__(self):
        return u"{0}".format(self.name)


class Component(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=generate_component_id, editable=False)
    category = models.ForeignKey(Category, null=False, blank=False)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    total_quantity = models.PositiveIntegerField(null=True, blank=True, default=0)
    being_used = models.PositiveIntegerField(null=True, blank=True, default=0)
    being_repaired = models.PositiveIntegerField(null=True, blank=True, default=0)
    being_purchased = models.PositiveIntegerField(null=True, blank=True, default=0)
    notes = models.TextField(null=True, blank=True)
    available_quantity = models.PositiveIntegerField(editable=False, default=0)

    class Meta:
        db_table = 'components'
        ordering = ['category', '-available_quantity',]

    def __unicode__(self):
        return u"{0} [{1}]".format(self.name, self.available_quantity)

    def get_absolute_url(self):
        return "/component/%s/edit/" % self.id

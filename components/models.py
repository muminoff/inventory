from django.db import models
import random
import string


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

    def __unicode__(self):
        return u"{0} [{1}]".format(self.name, self.available_quantity)

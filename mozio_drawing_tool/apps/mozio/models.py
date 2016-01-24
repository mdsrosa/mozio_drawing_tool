from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Company(BaseModel):
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        db_table = 'companies'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __unicode__(self):
        return self.name

class ServiceAreaCompany(BaseModel):
    company = models.ForeignKey(Company, related_name='company')

    class Meta:
        db_table = 'companies_service_areas'
        verbose_name = 'Company Service Area'
        verbose_name_plural = 'Company Service Areas'


    @classmethod
    def latest(cls):
        latests = cls.objects.select_related().order_by('-created_at')
        if latests.count() > 0:
            return latests[0]
        return latests

class Point(BaseModel):
    service_area = models.ForeignKey(ServiceAreaCompany, related_name='points')
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        db_table = 'service_area_points'
        ordering = ['-created_at']
        verbose_name = 'Service Area Point'
        verbose_name_plural = 'Service Area Points'

    def __unicode__(self):
        return 'Point (%.6f, %.6f)' % (self.latitude, self.longitude)
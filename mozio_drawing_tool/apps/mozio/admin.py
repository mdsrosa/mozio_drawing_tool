from django.contrib import admin

from .models import Company, ServiceAreaCompany, Point

admin.site.register(Company)
admin.site.register(ServiceAreaCompany)
admin.site.register(Point)
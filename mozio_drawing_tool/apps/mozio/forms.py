from django import forms
from .models import Company, ServiceAreaCompany, Point

class CreateServiceAreaForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    latitude_and_longitude = forms.CharField(max_length=255, required=False)

    widgets = {
        'latitude_and_longitude': forms.HiddenInput()
    }

    def save(self, points):
        data = self.cleaned_data

        # creates a relationship between Company and a Service Area
        company = data.get('company')
        service_area = ServiceAreaCompany(company=company)
        service_area.save()

        # handling latitude and longitudes
        total_points = len(points)

        service_area_points = []

        # save each point
        for point in points:
            latitude, longitude = point.split('&')
            latitude = latitude.split('=')[1]
            longitude = longitude.split('=')[1]

            point_object = Point(service_area=service_area, latitude=latitude,
                            longitude=longitude)
            point_object.save()

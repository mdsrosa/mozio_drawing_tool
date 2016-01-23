from django import forms
from .models import Company, ServiceAreaCompany, Point

class CreateServiceAreaForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all())

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

    def get_error_messages(self, show_field_label=True,
                            show_field_name=False, line_breaker='\n'):

        messages = ""

        if self.errors:
            for field in self:
                if field.errors:
                    if show_field_name:
                        messages += str(field.name).upper() + ': ' + field.errors.as_text()
                    elif show_field_label:
                        messages += field.label.capitalize().upper() + ': ' + field.errors.as_text()
                    else:
                        messages += field.errors.as_text()

                    messages = messages + line_breaker

        elif self.non_field_errors():

            for error in self.non_field_errors():
                messages += str(error) + line_breaker

        return messages

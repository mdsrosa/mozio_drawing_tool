from django.shortcuts import render_to_response, redirect
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext

from .forms import CreateServiceAreaForm
from .models import ServiceAreaCompany


def index(request):
    latest_service_area = ServiceAreaCompany.latest

    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
        'form': CreateServiceAreaForm,
        'latest_service_area': latest_service_area
    }

    return render_to_response('mozio/index.html', context,
                              context_instance=RequestContext(request))

def create_service_area(request):
    if request.method == 'POST':
        form = CreateServiceAreaForm(request.POST)
        if form.is_valid():
            # points must be sent like a list
            points = request.POST.getlist('latitude_and_longitude[]')

            # if points were provided, proceed
            if len(points) > 0:
                form.save(points)
                messages.success(request, _('Success! Your Service Area was saved!'))
            else:
                messages.error(request, _('No points were provided.'))
        else:
            messages.error(request, _(form.get_error_messages()))

        return redirect('mozio_index')

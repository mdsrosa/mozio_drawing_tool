from django.shortcuts import render_to_response, redirect
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext

from .forms import CreateServiceAreaForm


def index(request):
    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
        'form': CreateServiceAreaForm
    }

    return render_to_response('mozio/index.html', RequestContext(request, context))

def create_service_area(request):
    if request.method == 'POST':
        form = CreateServiceAreaForm(request.POST)
        if form.is_valid():
            points = request.POST.getlist('latitude_and_longitude[]')
            form.save(points)
            messages.success(request, _('Success! Your Service Area was saved!'))
        else:
            messages.error(request, _('Invalid form: %s' % form.errors))

        return redirect('mozio_index')

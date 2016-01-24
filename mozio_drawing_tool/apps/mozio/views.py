from django.shortcuts import render_to_response, redirect
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings

from .forms import CreateServiceAreaForm
from .models import ServiceAreaCompany, Point


def index(request):
    """
    This view is responsible for the interface where the user can define
    a service area.
    """
    latest_service_area = ServiceAreaCompany.latest

    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
        'form': CreateServiceAreaForm,
        'latest_service_area': latest_service_area
    }

    return render_to_response('mozio/index.html', context,
                              context_instance=RequestContext(request))

def create_service_area(request):
    """
    This view is responsible for saving the Service Area into the database.
    """
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

def validate_point(request):
    """
    This view is responsible for providing a map where you can
    click on any point on the map and find out if that point is
    within the bounding box.
    """
    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    }

    return render_to_response('mozio/validate_point.html', context, context_instance=RequestContext(request))

def points_json(request):
    """
    This view is responsible for providing the points of every service area
    in a jSON format.
    """
    service_areas = ServiceAreaCompany.objects.select_related().all()

    points_list = []

    for service_area in service_areas:
        service_area_points = service_area.points.all()
        points = []

        # todo: this could be cached
        for point in service_area_points:
            points.append({'lat': float(point.latitude),
                           'lng': float(point.longitude)})
        points_list.append({
            'company_name': service_area.company.name,
            'points': points
        })

    return JsonResponse(points_list, safe=False)
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings


class IndexView(View):
    template_name = 'mozio/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
        })

from django.conf.urls import url
from mozio_drawing_tool.apps.mozio.views import IndexView

urlpatterns = [
    url(r'^index$', IndexView.as_view(), name='mozio_index')
]
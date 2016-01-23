from django.conf.urls import url
from mozio_drawing_tool.apps.mozio import views

urlpatterns = [
    url(r'^index$', views.index, name='mozio_index')
]
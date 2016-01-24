from django.conf.urls import url
from mozio_drawing_tool.apps.mozio import views

urlpatterns = [
    url(r'^index$', views.index, name='mozio_index'),
    url(r'^service-area/create$', views.create_service_area,
        name='mozio_create_service_area'),
    url(r'^validate-point/$', views.validate_point,
        name='mozio_validate_point'),
    url(r'^points/json', views.points_json,
        name='mozio_json_points')
]
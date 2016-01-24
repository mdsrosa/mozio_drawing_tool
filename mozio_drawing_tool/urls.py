from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from mozio_drawing_tool.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'mozio/', include('mozio_drawing_tool.apps.mozio.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

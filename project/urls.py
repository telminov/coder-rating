from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')

urlpatterns = [
    path('', RedirectView.as_view(url='/backend/')),
    path('backend/', schema_view),
    path('backend/', include('core.urls')),
    path('backend/admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static('backend/media', document_root=settings.MEDIA_ROOT)

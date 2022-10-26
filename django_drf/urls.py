from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

api_info = openapi.Info(
    title="Snippets API",
    default_version='1.0.0',
    description='API documentation of App',
)

schema_view = get_schema_view(
    openapi.Info(
        title="Printer API",
        default_version='1.0.0',
        description='API documentation of App',
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('', include(('drf_api.urls', 'printer'), namespace='printers')),
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-shema')
    ])),
]

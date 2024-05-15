# from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
# from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

# from .api import api_router

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    # path("search/", search_views.search, name="search"),
]

urlpatterns = urlpatterns + []

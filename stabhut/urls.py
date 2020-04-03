from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from stabhut.settings import ADMIN_URL

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    path("docs/", include_docs_urls(title="StabHut API")),
    path("auth/", include("rest_framework.urls")),
    path("auth/", obtain_jwt_token),
    path("api/", include("api.urls")),
]

from django.contrib import admin
from django.urls import include, path  # new
# Настраиваем URLS
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("snippets.urls")),  # new
]

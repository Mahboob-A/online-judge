from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("submit/", include("core_apps.judge_engine.urls")),
]

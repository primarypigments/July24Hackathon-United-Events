from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("index.urls")),
    path("contact/", include("contact.urls")),
    path("events/", include("events.urls")),
    path("profile/", include("profiles.urls")),
]

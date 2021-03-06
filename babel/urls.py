"""
babel URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from catalog.views import home, newsroom, about, publication
from catalog.viewscat import PublicationByDewey, PublicationDetail

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("newsroom/", newsroom, name="newsroom"),
        path("about/", about, name="about"),
        path("catalog/", publication, name="publication"),
        path(
            "catalog/dewey_<str:deweynumber>/",
            PublicationByDewey.as_view(),
            name="publication-dewey",
        ),
        path(
            "catalog/<int:deweynumber>_<str:authorref>_<pk>/",
            PublicationDetail.as_view(),
            name="publication-detail",
        ),
        path(
            "catalog/<pk>/", PublicationDetail.as_view(), name="publication-detail-pk",
        ),
        path("", home, name="home"),
    ]
    
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

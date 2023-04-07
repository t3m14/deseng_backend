from django.urls import path, include, re_path

urlpatterns = [
    path(r'', include('djoser.urls')),
    re_path(r'', include('djoser.urls.authtoken')),
]
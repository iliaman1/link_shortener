from django.urls import path

from apps.shortener.views import SmartUrlCreateView


urlpatterns = [
    path('', SmartUrlCreateView.as_view(), name='smarturl-create')
]

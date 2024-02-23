from django.urls import path

from apps.shortener.views import SmartUrlRedirectCreateView

urlpatterns = [
    path('', SmartUrlRedirectCreateView.as_view(), name='smarturl-create'),
    path('<str:token>', SmartUrlRedirectCreateView.as_view(), name='smarturl-redirect')
]

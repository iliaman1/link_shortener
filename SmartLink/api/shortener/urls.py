from django.urls import path

from apps.shortener.views import SmartUrlCreateView, SmartUrlRedirect

urlpatterns = [
    path('<str:token>', SmartUrlRedirect.as_view(), name='smarturl-redirect'),
    path('', SmartUrlCreateView.as_view(), name='smarturl-create')
]

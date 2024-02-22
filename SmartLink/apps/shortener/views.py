from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import SmartUrlSerializer
from django.shortcuts import redirect
from .models import SmartUrl


class SmartUrlRedirect(APIView):
    def get(self, request, *args, **kwargs):
        token = kwargs.get('token', None)
        if token:
            url = SmartUrl.objects.get(short_url__exact=token)
            return redirect(url.full_url)


class SmartUrlCreateView(CreateAPIView):
    serializer_class = SmartUrlSerializer

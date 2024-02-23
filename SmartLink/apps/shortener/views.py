from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import CreateModelMixin
from .serializers import SmartUrlSerializer
from django.shortcuts import redirect
from .models import SmartUrl


class SmartUrlRedirectCreateView(GenericAPIView, CreateModelMixin):
    serializer_class = SmartUrlSerializer

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(SmartUrl.objects.only('full_url'), short_url__exact=kwargs.get('token'))
        return redirect(obj.full_url)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

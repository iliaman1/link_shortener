from rest_framework.generics import CreateAPIView
from .serializers import SmartUrlSerializer


class SmartUrlCreateView(CreateAPIView):
    serializer_class = SmartUrlSerializer

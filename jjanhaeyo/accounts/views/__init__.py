from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from accounts.serializers import ConfigSerializer
from accounts.models import Config


class ConfigViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ConfigSerializer
    http_method_naems = ['get']

    def get_queryset(self):
        return Config.objects.all()

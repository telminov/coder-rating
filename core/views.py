from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import permissions
from core import models
from core import serializers


class CoderViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = models.Coder.objects.all()
    serializer_class = serializers.Coder

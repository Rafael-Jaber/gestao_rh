from apps.registro_hora_extra.models import RegistroHoraExtra
from rest_framework import viewsets
from .serializers import RegistroHoraExtraSerializer



class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer

from django.views.generic.edit import CreateView
from .models import Documento


class DucmentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']



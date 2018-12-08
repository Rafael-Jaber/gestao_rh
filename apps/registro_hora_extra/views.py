import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraUpdate(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraUpdateFun(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'horas']

    def get_success_url(self):
        return reverse_lazy('update_funcionario', args=[self.object.funcionario.id])


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora-extra')


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraCreateFun(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'horas']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('update_funcionario', args=[self.object.funcionario.id])


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):

        registro_hora = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora.utilizada = True
        registro_hora.save()

        empregado = self.request.user.funcionario

        response = json.dumps({
            'mensagem': 'Requisição executada',
            'horas': float(empregado.total_horas_extra)
        })

        return HttpResponse(response, content_type='application/json')

from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        object = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = object
        funcionario.save()
        return HttpResponse('Ok')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']
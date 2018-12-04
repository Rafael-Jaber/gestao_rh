from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    
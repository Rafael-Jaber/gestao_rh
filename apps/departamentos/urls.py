from django.urls import path
from .views import (
    DepartamentosList,
    DepartamentoCreate,
)

urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo/', DepartamentoCreate.as_view(), name='create_departamento'),
]

from django.urls import path
from .views import DepartamentosList

urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
]

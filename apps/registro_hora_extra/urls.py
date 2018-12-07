from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraUpdate,
    HoraExtraDelete

)

urlpatterns = [
    path('', HoraExtraList.as_view(), name="list_hora-extra"),
    path('editar/<int:pk>', HoraExtraUpdate.as_view(), name="update_hora-extra"),
    path('deletar/<int:pk>', HoraExtraDelete.as_view(), name="delete_hora-extra"),
    #path('novo/', FuncionarioNovo.as_view(), name="create_funcionario"),
]

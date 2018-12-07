from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraUpdate

)

urlpatterns = [
    path('', HoraExtraList.as_view(), name="list_hora-extra"),
    path('editar/<int:pk>', HoraExtraUpdate.as_view(), name="update_hora-extra"),
    #path('deletar/<int:pk>', FuncionarioDelete.as_view(), name="delete_funcionario"),
    #path('novo/', FuncionarioNovo.as_view(), name="create_funcionario"),
]

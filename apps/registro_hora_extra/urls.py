from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraUpdate,
    HoraExtraDelete,
    HoraExtraCreate,
    HoraExtraUpdateFun,
    HoraExtraCreateFun

)

urlpatterns = [
    path('', HoraExtraList.as_view(), name="list_hora-extra"),
    path('editar/<int:pk>', HoraExtraUpdate.as_view(), name="update_hora-extra"),
    path('editar-funcionario/<int:pk>', HoraExtraUpdateFun.as_view(), name="update_hora-extra-fun"),
    path('deletar/<int:pk>', HoraExtraDelete.as_view(), name="delete_hora-extra"),
    path('novo/', HoraExtraCreate.as_view(), name="create_hora-extra"),
    path('novo/<int:funcionario_id>', HoraExtraCreateFun.as_view(), name="create_hora-fun"),
]

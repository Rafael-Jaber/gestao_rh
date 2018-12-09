from django.urls import path
from .views import (
    FuncionariosList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioNovo,
    Pdf
)

from .views import pdf_reportlab


urlpatterns = [
    path('', FuncionariosList.as_view(), name="list_funcionarios"),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name="update_funcionario"),
    path('deletar/<int:pk>', FuncionarioDelete.as_view(), name="delete_funcionario"),
    path('novo/', FuncionarioNovo.as_view(), name="create_funcionario"),
    path('pdf_reportlab', pdf_reportlab, name='gerar_pdf_reportlab'),
    path('pdf_html', Pdf.as_view(), name='gerar_pdf_html'),
]

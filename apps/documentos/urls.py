from django.urls import path
from .views import DucmentoCreate

urlpatterns = [
    path('novo/', DucmentoCreate.as_view(), name="create_documento"),
]

from django.urls import path
from .views import *

urlpatterns = [
    path("<int:id>/", carro_detalhe, name='carro_detalhe')
]

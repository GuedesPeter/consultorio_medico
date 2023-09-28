from django.urls import path
from medicSearch.views.ProfileView import list_profile_view

urlpatterns = [
    # Duas linhas chamando a mesma URL
    path("", list_profile_view), # Chama o metodo sem passar ID (ID deve estar setado como NONE dentro do metodo para não gerar erro)
    path("<int:id>", list_profile_view), #URL CUSTOMIZADA onde o ID recebe um valor inteiro (neste caso o ID não será NONE)
]

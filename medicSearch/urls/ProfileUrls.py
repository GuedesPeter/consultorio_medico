from django.urls import path
from medicSearch.views.ProfileView import list_profile_view

urlpatterns = [
    # Duas linhas chamando a mesma URL
    path("", list_profile_view, name='profiles'), # Chama o metodo sem passar ID (ID deve estar setado como NONE dentro do metodo para não gerar erro)
    path("<int:id>", list_profile_view, name='profile'), #URL CUSTOMIZADA onde o ID recebe um valor inteiro (neste caso o ID não será NONE)
]
# Foram inseridos os atributos NAME em cada url para personalização dos links
# Caso seja necessário trocar a url de view, Não será preciso mexer em cada template da aplicação
# pois o atributo NAME funcionará como uma VARIÀVEL 
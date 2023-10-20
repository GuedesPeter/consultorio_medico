from django.shortcuts import render
from medicSearch.models import Profile # Importando a model Profile
from django.db.models import Q # Funciona como OR no sql
from django.core.paginator import Paginator


def list_medics_view(request):
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get("neighborhood")
    city = request.GET.get("city")
    state = request.GET.get("state")
 
    medics = Profile.objects.filter(role=2).all() # filtra todos os perfis do tipo médico
    
# Busca por: NOME - ESPECIALIDADE -BAIRRO - CIDADE - ESTADO
    if name is not None and name != '':
        #Filtra o nome buscado tanto em (Q)first_name quanto em (Q)user name 
        medics = medics.filter(Q(user__first_name=name) | Q(user__username__contains=name))
    if speciality is not None:
        medics = medics.filter(specialties__id=speciality)

    if neighborhood is not None:
        medics = medics.filter(addresses__neighborhood=neighborhood)
    else:
        if city is not None:
            medics = medics.filter(addresses__neighborhood__city=city)
        elif state is not None:
            medics = medics.filter(addresses__neighborhood__city__state=state)

    #Paginação - Implementando a classe Paginator
    if len(medics) > 0:
        paginator = Paginator(medics, 8) # Objeto de consulta e qtde. retornada para o html.
        page = request.GET.get('page') # Obtem as páginas
        medics = paginator.get_page(page) # Verifica qual página foi selecionada pelo usuário e gera resultado como base nela.


    #Soluciona o problema de perda de parâmetros da url quando há troca de página
    get_copy = request.GET.copy() #Copia os parametros da url atual
    parameters = get_copy.pop('page', True) and get_copy.urlencode() #Remove o parametro 'page' atual e faz com que não se perca os
    #parametros da url atual ao trocar de página

    context = { 
        'medics': medics,
        'parameters': parameters
    }
       
    return render(request, template_name='medic/medics.html', context=context, status=200)


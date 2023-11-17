from django.shortcuts import render, redirect
from medicSearch.models import Profile, Rating # Importando a model Profile e Rating
from medicSearch.forms.MedicForm import MedicRatingForm
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


def add_favorite_view(request):
    page = request.POST.get("page")
    name = request.POST.get("name")
    speciality = request.POST.get("speciality")
    neighborhood = request.POST.get("neighborhood")
    city = request.POST.get("city")
    state = request.POST.get("state")
    id = request.POST.get("id")

    try:
        profile = Profile.objects.filter(user=request.user).first()
        medic = Profile.objects.filter(user__id=id).first()
        profile.favorites.add(medic.user)
        profile.save()
        msg = "Favorito adicionado com sucesso"
        _type = "success"
    except Exception as e:
        print("Erro %s" % e)
        msg = "Um erro ocorreu ao salvar o médico nos favoritos"
        _type = "danger"

    if page:
        arguments = "?page=%s" % (page)
    else:
        arguments = "?page=1"
    if name:
        arguments += "&name=%s" % name
    if speciality:
        arguments += "&specinality=%s" % speciality
    if neighborhood:
        arguments += "&neighborhood=%s" % neighborhood
    if city:
        arguments += "&city=%s" % city
    if state:
        arguments += "&state=%s" % state

    arguments += "&msg=%s&type=%s" % (msg, _type)

    return redirect(to='/medic/%s' % arguments)


def remove_favorite_view(request):
    page = request.POST.get("page")
    id = request.POST.get("id")

    try:
        profile = Profile.objects.filter(user=request.user).first()
        medic = Profile.objects.filter(user__id=id).first()
        profile.favorites.remove(medic.user)
        profile.save()
        msg = "Favorito removido com sucesso."
        _type = "success"
    except Exception as e:
        print("Erro %s" % e)
        msg = "Um erro ocorreu ao remover o médico nos favoritos."

        _type = "danger"

        if page:
            arguments = "?page=%s" % (page)
        else:
            arguments = "?page=1"

        arguments += "&msg=%stype=%s" % (msg, _type)

        return redirect(to='/profile/%s' % arguments)


def rate_medic(request, medic_id=None):
    medic = Profile.objects.filter(user__id=medic_id).first()
    rating = Rating.objects.filter(user=request.user, user_rated=medic.user).firts()
    message = None
    initial = {'user': request.user, 'user_rated': medic.user}

    if request.method == 'POST':
        ratingForm = MedicRatingForm(request.POST, instance=rating, initial=initial)
    else:
        ratingForm = MedicRatingForm(instance=rating, initial=initial)
    
    if ratingForm.is_valid():
        ratingForm.save()
        message = {'type': 'success', 'text': 'Avaliação salva com sucesso.'}
    else:
        if request.method == 'POST':
            message = {'type': 'danger', 'text': 'Erro ao salvar a avaliação.'}

    context = {
        'ratingForm': ratingForm,
        'medic': medic,
        'message': message
    }

    return render(request, template_name='medic/rating.html', context=context, status=200)

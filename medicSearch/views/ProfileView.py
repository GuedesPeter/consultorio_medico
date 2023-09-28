from django.http import HttpResponse


def list_profile_view(request, id=None):
    # Modificação para retornar o Usuário que está logado usando o parâmetro REQUEST
    if id is None and request.user.is_authenticated: # Se estiver logado (request.user.is_authenticated)
        id = request.user.id # Retorna o ID do usuário logado
    elif not request.user.is_authenticated: # Se NÂO estiver logado (NOT request.user.is_authenticated)
        id = 0 # Retorna o ID com o valor zero
    return HttpResponse('<h1>Usuário de id %s!</h1>' % id)
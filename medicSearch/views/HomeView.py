from django.http import HttpResponse # Importa a classe HttpResponse permitindo retornar a resposta para o CLIENT

# Método que vamos disparar através da URL
# REQUEST: Parametro padrão da VIEW que recupera da dos da requisição (GET ou POST)
def home_view(request):
    return HttpResponse('<h1>Olá mundo!</h1>')
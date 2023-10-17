from django.shortcuts import render

# Método que vamos disparar através da URL
# REQUEST: Parametro padrão da VIEW que recupera da dos da requisição (GET ou POST)
def home_view(request):
    return render(request, template_name='home/home.html', status=200)
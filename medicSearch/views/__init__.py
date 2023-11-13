# Aqui dizemos ao Django que, entre todos os arquivos que estão na pasta VIEWS,
# apenas os que tiverem importados dentro de __init__.py poderão ser usados dentro da aplicação
from .HomeView import *
from .ProfileView import * 
from .MedicView import * 
from .AuthView import * 
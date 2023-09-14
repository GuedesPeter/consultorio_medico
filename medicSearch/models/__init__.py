'''Bibliotecas importadas para que todas as MODELS que forem importadas DEPOIS delas possam
USA-LAS sem precisar importar separadamente em seus arquivos'''
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Variável chamada dentro do arquivo Profile.py
ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Médico'),
    (3, 'Paciente')
)

# IMPORTAÇÃO DAS MODELS -----------------------------------------------
'''TODA VEZ que quisermos que uma MODEL se TORNE UMA TABELA do Banco de Dados,
 precisamo IMPORTA-LA neste arquivo (__INIT__.PY)'''
 
# Models importadas (Se tornaram TABELAS do Banco de Dados)
from .Rating import Rating
from .DayWeek import DayWeek
from .State import State
from .City import City
from .Neighborhood import Neighborhood
from .Address import Address
from .Speciality import Speciality
from .Profile import Profile 
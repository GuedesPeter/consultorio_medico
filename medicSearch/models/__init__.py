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

# IMPORTAÇÃO DA MODEL PROFILE -----------------------------------------------
'''TODA VEZ que quisermos que uma MODEL se TORNE UMA TABELA do Banco de Dados,
 precisamo IMPORTA-LA neste arquivo (__INIT__.PY)'''
 
# Model importada (Se tornou uma tabela do Banco de Dados)

from .Profile import Profile 
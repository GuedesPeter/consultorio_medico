from django.contrib import admin
from .models import *  # IMPORTA AS MODELS PARA REGISTRO ---------

# CUSTOMIZANDO A MODEL PROFILE --------------------------------
class ProfileAdmin(admin.ModelAdmin):
    # CRIA UM FILTRO DE HIERARQUIA COM DATAS ------------------------
    date_hierarchy = 'created_at'
    # PERMITE DIZER AO DJANGO OS ELEMENTOS EXIBIDOS NA LISTAGEM DE DADOS DA MODEL -------
    list_display = ['user', 'role', 'birthday']
    # PERMITE ALTERAR A APRESENTAÇÃO DOS CAMPOS VAZIOS EM NOSSO SISTEMA ----------------
    empty_value_display = 'Vazio'
    # DEIXA OUTRAS LINHAS COM LINK DE EDIÇÃO HABILITADO
    list_display_links = ['user', 'role']
    # PERMITE CRIAR UM FILTRO DE DADOS BASEADO NOS CAMPOS QUE FOREM ADICIONADOS A ESSA LISTA
    # OBS: Para acessar um atributo da Foreing Key (user) que faz referencia a model de usuário
    # foi necessario chamar o atributo 'user' e passar dois underlines(ANTES DE is_active) para separa-lo
    # do atributo que faz referencia a model USER 
    list_filter = ['user__is_active','role']
    # PERMITE DIZER QUAIS CAMPOS SERÃO EXIBIDOS NO FORMULÁRIO E QUAIS NÃO
    # OBS: Um campo que seja NOT NULL sem valor default devera ser adicionado na listagem,
    # do contrario um erro ocorrerá na hora de salvar o dado, dizendo que o campo NOT NULL
    # NÃO PODERÁ FICAR EM BRANCO
    fields = ['user',('role'), 'image', 'birthday', 'specialties', 'adresses']
    # OPOSTO DO FIELDS - REMOVERÁ DO FORMULÁRIO OS CAMPO QUE FOREM ADICIONADOS A LISTA
    exclude = ['favorites', 'created_at', 'updated_at']
    # DEIXA OS CAMPOS APENAS COMO LEITURA NO FORMULARIO DE EDIÇÃO E CRIAÇÃO
    # Usado para que NÃO SEJA PERMITIDO alterar o usuário atrelado ao perfil
    # Aplica o recurso na edição e criação
    readonly_fields = ['user']
    # CAMPOS QUE PODERÃO SER PESQUISADOS NA TELA DO ADMIN
    # Os campos que representam relacionamento pracisamos colocar:
    # NOME DO CAMPO - dois UNDERLINES - NOME DO ATRIBUTO QUE SERÁ PESQUISADO
    search_fields = ['user__username']





# Register your models here.
admin.site.register(Profile, ProfileAdmin)  # Model ProfileAdmin REGISTRADA ----------------
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
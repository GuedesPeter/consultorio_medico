from django.contrib import admin
from .models import *  # IMPORTA AS MODELS PARA REGISTRO ---------

# CUSTOMIZANDO A MODEL PROFILE --------------------------------
class ProfileAdmin(admin.ModelAdmin):
    # CRIA UM FILTRO DE HIERARQUIA COM DATAS ------------------------
    date_hierarchy = 'created_at'



# Register your models here.
admin.site.register(Profile, ProfileAdmin)  # Model ProfileAdmin REGISTRADA ----------------
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
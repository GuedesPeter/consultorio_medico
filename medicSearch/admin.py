from django.contrib import admin
from .models import *  # IMPORTA AS MODELS PARA REGISTRO ---------

# CUSTOMIZANDO A MODEL PROFILE --------------------------------
class ProfileAdmin(admin.ModelAdmin):
    
     date_hierarchy = 'created_at'
     list_display = ['user', 'birth', 'specialtiesList', 'addressesList']
     empty_value_display = 'Vazio'
     #list_display_links = ['user', 'specialtiesList', 'adressesList']
     list_filter = ['user__is_active','role']
    #fields = ['user',('role'), 'image', 'birthday', 'specialties', 'adresses']
     exclude = ['favorites', 'created_at', 'updated_at']
     readonly_fields = ['user']
     search_fields = ['user__username']
     # Avançado ----------------------------------------------------------------
     fieldsets = [
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields': ('role', )
        }),
        ('Extras', {
            'fields': ('specialties', 'adresses')
        })
    ]
    # Custom List_display --------------------------------------------------
    # list_display = ['user', 'birth']
     def birth(self,obj):
          if obj.birthday:
               return obj.birthday.strftime('%d-%m-%Y')
          
    # Custom empty_value_display --------------------------------------------      
     def birth(self,obj):
          if obj.birthday:
               return obj.birthday
     birth.empty_value_display = '__/__/____'

     # Custom List_display ManyTo Many ------------------------------------------------
     def specialtiesList(self, obj):
          for i in obj.specialties.all():
               return [i.name]
     def addressesList(self, obj):
          return [i.name for i in obj.addresses.all()]
     
     # ADICIONANDO ARQUIVOS CSS E JS ---------------------------------------------------
     class Media:
        css = {
              "all": ("css/custom.css")
        }
        js = ("js/custom.js")       
    


# Register your models here.
admin.site.register(Profile, ProfileAdmin)  # Model ProfileAdmin REGISTRADA ----------------
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
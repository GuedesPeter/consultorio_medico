
from django.conf import settings
#  IMPORTAÇÕES PARA UPLOAD DE IMAGENS -------------------------
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

#  + STATIC ADICIONADO SAO FINAL DE URLPATTERNS ------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    # Adiciona as URLS do meu app MEDICSEARCH (medicsearch/urls/NOME DA URL) --------------------------------
    path('',include('medicSearch.urls.HomeUrls')),
    path('', include('medicSearch.urls.AuthUrls')), 
    path('profile/', include('medicSearch.urls.ProfileUrls')), # PASSAR O PREFIXO QUE REFERENCIA A URL CRIADA (profile/)
    path('medics/', include('medicSearch.urls.MedicUrls')), # PASSAR O PREFIXO QUE REFERENCIA A URL CRIADA (medic/)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

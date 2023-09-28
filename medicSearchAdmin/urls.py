"""
URL configuration for medicSearchAdmin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('profile/', include('medicSearch.urls.ProfileUrls')), # PASSAR O PREFIXO QUE REFERENCIA A URL CRIADA (profile/)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

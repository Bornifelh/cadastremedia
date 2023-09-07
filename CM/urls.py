"""
URL configuration for CM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import etat_content
from .views.accueil import main_content
from .views.etat_content import etat_nat_content
from .views.institution_content import in_internationale, in_nationale
from .views.rs_content import facebook_content, facebook_tiktok, facebook_twitter, facebook_youtube
from .views.ml_content import mel_nationaux, mel_internationaux

urlpatterns = [
    path('', main_content, name="index"),
    path('rs/facebook/', facebook_content, name="rs/facebook"),
    path('rs/tiktok/', facebook_tiktok, name="rs/tiktok"),
    path('rs/twitter/', facebook_twitter, name="rs/twitter"),
    path('rs/youtube/', facebook_youtube, name="rs/youtube"),

    # --------etat----------
    path('etat/et_etat/', etat_nat_content, name="etat/et_etat"),

    # --------mel ----------
    path('ml/mel_internationaux/', mel_internationaux, name="ml/mel_internationaux/"),
    path('ml/mel_nationaux/', mel_nationaux, name="ml/mel_nationaux/"),

    # --------mel ----------
    path('ml/mel_internationaux/', mel_internationaux, name="ml/mel_internationaux/"),
    path('ml/mel_nationaux/', mel_nationaux, name="ml/mel_nationaux/"),

    # --------in ----------
    path('in/in_internationle/', in_internationale, name="in/in_internationle/"),
    path('in/in_nationle/', in_nationale, name="in/in_nationle/"),

    # --------in ----------
    path('frm/frm_whatsapp/', in_internationale, name="frm/frm_whatsapp/"),
    path('frm/frm_autres/', in_nationale, name="frm/frm_autres/"),
]

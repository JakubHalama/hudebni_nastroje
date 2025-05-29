from django.urls import path
from . import views

urlpatterns = [
    path('', views.seznam_nastroju, name='seznam_nastroju'),
    path('nastroj/<int:pk>/', views.detail_nastroje, name='detail_nastroje'),
    path('nastroj/pridat/', views.vytvor_nastroj, name='vytvor_nastroj'),
    path('nastroj/<int:pk>/upravit/', views.upravit_nastroj, name='upravit_nastroj'),
    path('nastroj/<int:pk>/smazat/', views.smazat_nastroj, name='smazat_nastroj'),  # Přidáme tuto cestu pro smazání
    path('nastroj/<int:pk>/potvrdit_smazani/', views.potvrdit_smazani, name='potvrdit_smazani'),  # Cesta pro potvrzení smazání
]

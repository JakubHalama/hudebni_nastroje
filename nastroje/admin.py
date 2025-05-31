from django.contrib import admin
from .models import HudebniNastroj, Vyrobce

@admin.register(Vyrobce)
class VyrobceAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'zeme')
    search_fields = ('nazev', 'zeme')
    list_filter = ('zeme',)

@admin.register(HudebniNastroj)
class HudebniNastrojAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'vyrobce', 'typ', 'cena')
    list_filter = ('typ', 'vyrobce')
    search_fields = ('nazev', 'vyrobce__nazev')
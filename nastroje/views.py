from django.shortcuts import render, get_object_or_404, redirect
from .models import HudebniNastroj, Vyrobce
from django.contrib import messages
from .forms import HudebniNastrojForm, VyrobceForm
from django.db import models
from django.http import JsonResponse

# Seznam všech nástrojů
def home(request):
    nove_nastroje = HudebniNastroj.objects.all().order_by('-id')[:3]  # Get 3 most recent instruments
    return render(request, 'nastroje/home.html', {
        'typy_nastroju': HudebniNastroj.TYPY_NASTROJU,
        'nove_nastroje': nove_nastroje
    })

def seznam_nastroju(request):
    query = request.GET.get('q', '')
    selected_type = request.GET.get('typ', '')
    nastroje = HudebniNastroj.objects.all()
    
    if query:
        nastroje = nastroje.filter(
            models.Q(nazev__icontains=query) |
            models.Q(vyrobce__nazev__icontains=query) |
            models.Q(typ__icontains=query) |
            models.Q(material__icontains=query) |
            models.Q(popis__icontains=query)
        )
    
    if selected_type:
        nastroje = nastroje.filter(typ=selected_type)
    
    return render(request, 'nastroje/seznam.html', {
        'nastroje': nastroje,
        'search_query': query,
        'selected_type': selected_type,
        'typy_nastroju': HudebniNastroj.TYPY_NASTROJU
    })

# Detail nástroje
def detail_nastroje(request, pk):
    nastroj = get_object_or_404(HudebniNastroj, pk=pk)
    return render(request, 'nastroje/detail.html', {'nastroj': nastroj})

# Vytvoření nového nástroje
def vytvor_nastroj(request):
    if request.method == 'POST':
        form = HudebniNastrojForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seznam_nastroju')
    else:
        form = HudebniNastrojForm()
    return render(request, 'nastroje/form.html', {'form': form})

# Úprava existujícího nástroje
def upravit_nastroj(request, pk):
    nastroj = get_object_or_404(HudebniNastroj, pk=pk)
    if request.method == 'POST':
        form = HudebniNastrojForm(request.POST, request.FILES, instance=nastroj)
        if form.is_valid():
            form.save()
            return redirect('detail_nastroje', pk=nastroj.pk)
    else:
        form = HudebniNastrojForm(instance=nastroj)
    return render(request, 'nastroje/form.html', {'form': form})

# Funkce pro potvrzení smazání
def potvrdit_smazani(request, pk):
    nastroj = get_object_or_404(HudebniNastroj, pk=pk)
    if request.method == 'POST':
        # Pokud uživatel klikne na potvrdit, smažeme nástroj
        nastroj.delete()
        messages.success(request, "Nástroj byl úspěšně smazán.")
        return redirect('seznam_nastroju')
    return render(request, 'nastroje/potvrdit_smazani.html', {'nastroj': nastroj})

# Funkce pro smazání nástroje (zastaralá - již nepotřebná, protože přesměrování bude do `potvrdit_smazani`)
def smazat_nastroj(request, pk):
    nastroj = get_object_or_404(HudebniNastroj, pk=pk)
    return redirect('potvrdit_smazani', pk=nastroj.pk)

def vytvorit_vyrobce(request):
    if request.method == 'POST':
        form = VyrobceForm(request.POST, request.FILES)
        if form.is_valid():
            vyrobce = form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'id': vyrobce.id,
                    'nazev': vyrobce.nazev
                })
            return redirect('seznam_nastroju')
    else:
        form = VyrobceForm()
    
    template = 'nastroje/vytvorit_vyrobce_popup.html' if request.headers.get('X-Requested-With') == 'XMLHttpRequest' else 'nastroje/vytvorit_vyrobce.html'
    return render(request, template, {'form': form})

def detail_vyrobce(request, pk):
    vyrobce = get_object_or_404(Vyrobce, pk=pk)
    return render(request, 'nastroje/detail_vyrobce.html', {'vyrobce': vyrobce})

def seznam_vyrobcu(request):
    vyrobci = Vyrobce.objects.all().order_by('nazev')
    return render(request, 'nastroje/seznam_vyrobcu.html', {
        'vyrobci': vyrobci,
        'typy_nastroju': HudebniNastroj.TYPY_NASTROJU
    })

def smazat_vyrobce(request, pk):
    vyrobce = get_object_or_404(Vyrobce, pk=pk)
    return redirect('potvrdit_smazani_vyrobce', pk=vyrobce.pk)

def potvrdit_smazani_vyrobce(request, pk):
    vyrobce = get_object_or_404(Vyrobce, pk=pk)
    if request.method == 'POST':
        vyrobce.delete()
        messages.success(request, "Výrobce byl úspěšně smazán.")
        return redirect('seznam_vyrobcu')
    return render(request, 'nastroje/potvrdit_smazani_vyrobce.html', {'vyrobce': vyrobce})

from django.shortcuts import render, get_object_or_404, redirect
from .models import HudebniNastroj
from django.contrib import messages
from .forms import HudebniNastrojForm

# Seznam všech nástrojů
def seznam_nastroju(request):
    nastroje = HudebniNastroj.objects.all()
    return render(request, 'nastroje/seznam.html', {'nastroje': nastroje})

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

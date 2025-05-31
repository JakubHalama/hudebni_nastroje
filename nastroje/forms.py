# nastroje/forms.py
from django import forms
from .models import HudebniNastroj, Vyrobce

class VyrobceForm(forms.ModelForm):
    class Meta:
        model = Vyrobce
        fields = ['nazev', 'zeme', 'popis', 'logo', 'web']
        widgets = {
            'nazev': forms.TextInput(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color focus:border-text-accent focus:ring-1 focus:ring-text-accent focus:ring-opacity-20 transition-all duration-300'
            }),
            'zeme': forms.TextInput(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color focus:border-text-accent focus:ring-1 focus:ring-text-accent focus:ring-opacity-20 transition-all duration-300'
            }),
            'popis': forms.Textarea(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color focus:border-text-accent focus:ring-1 focus:ring-text-accent focus:ring-opacity-20 transition-all duration-300',
                'rows': 4
            }),
            'logo': forms.ClearableFileInput(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color transition-all duration-300'
            }),
            'web': forms.URLInput(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color focus:border-text-accent focus:ring-1 focus:ring-text-accent focus:ring-opacity-20 transition-all duration-300'
            }),
        }

class HudebniNastrojForm(forms.ModelForm):
    class Meta:
        model = HudebniNastroj
        fields = ['nazev', 'vyrobce', 'typ', 'barva', 'cena', 'material', 'popis', 'obrazek']
        widgets = {
            'nazev': forms.TextInput(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color focus:border-text-accent focus:ring-1 focus:ring-text-accent focus:ring-opacity-20 transition-all duration-300'
            }),
            'vyrobce': forms.Select(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color focus:border-text-accent focus:ring-1 focus:ring-text-accent focus:ring-opacity-20 transition-all duration-300',
                'data-popup-url': '/nastroje/vytvorit-vyrobce/',
            }),
            'typ': forms.Select(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color focus:border-text-accent focus:ring-1 focus:ring-text-accent focus:ring-opacity-20 transition-all duration-300'
            }),
            'barva': forms.TextInput(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color focus:border-text-accent focus:ring-1 focus:ring-text-accent focus:ring-opacity-20 transition-all duration-300'
            }),
            'cena': forms.NumberInput(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color focus:border-text-accent focus:ring-1 focus:ring-text-accent focus:ring-opacity-20 transition-all duration-300'
            }),
            'material': forms.TextInput(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color focus:border-text-accent focus:ring-1 focus:ring-text-accent focus:ring-opacity-20 transition-all duration-300'
            }),
            'popis': forms.Textarea(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color focus:border-text-accent focus:ring-1 focus:ring-text-accent focus:ring-opacity-20 transition-all duration-300',
                'rows': 4
            }),
            'obrazek': forms.ClearableFileInput(attrs={
                'class': 'w-full px-6 py-4 text-text-primary rounded-xl bg-dark-accent/30 border border-border-color transition-all duration-300'
            }),
        }
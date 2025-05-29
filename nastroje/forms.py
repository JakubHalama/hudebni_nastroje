# nastroje/forms.py
from django import forms
from .models import HudebniNastroj

class HudebniNastrojForm(forms.ModelForm):
    class Meta:
        model = HudebniNastroj
        fields = ['nazev','vyrobce','typ','barva','cena','material', 'popis', 'obrazek']
        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control'}),
            'vyrobce': forms.TextInput(attrs={'class': 'form-control'}),
            'typ': forms.Select(attrs={'class': 'form-control'}),
            'barva': forms.TextInput(attrs={'class': 'form-control'}),
            'cena': forms.NumberInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}),
            'popis': forms.Textarea(attrs={'class': 'form-control'}),
            'obrazek': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        typ = forms.ChoiceField(choices=HudebniNastroj.TYPY_NASTROJU)
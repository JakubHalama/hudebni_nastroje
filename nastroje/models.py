from django.db import models

class Vyrobce(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název výrobce')
    zeme = models.CharField(max_length=100, verbose_name='Země původu', blank=True)
    popis = models.TextField(verbose_name='Popis výrobce', blank=True)
    logo = models.ImageField(upload_to='vyrobci/', blank=True, null=True)
    web = models.URLField(verbose_name='Webové stránky', blank=True)
    
    def __str__(self):
        return self.nazev
    
    class Meta:
        verbose_name = 'Výrobce'
        verbose_name_plural = 'Výrobci'
        ordering = ['nazev']

class HudebniNastroj(models.Model):
    TYPY_NASTROJU = [
        ('strunne', 'Strunné'),
        ('dechove', 'Dechové'),
        ('klavesove', 'Klávesové'),
        ('bici', 'Bicí'),
        ('jine', 'Jiné'),
    ]

    nazev = models.CharField(max_length=100)
    vyrobce = models.ForeignKey(Vyrobce, on_delete=models.CASCADE, related_name='nastroje', verbose_name='Výrobce')
    typ = models.CharField(max_length=20, choices=TYPY_NASTROJU)
    barva = models.CharField(max_length=50, null=True, blank=True)
    cena = models.IntegerField(null=True, blank=True)
    material = models.CharField(max_length=100, blank=True)
    popis = models.TextField(blank=True)
    obrazek = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.nazev

    class Meta:
        verbose_name = 'Hudební nástroj'
        verbose_name_plural = 'Hudební nástroje'

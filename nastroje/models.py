from django.db import models

class HudebniNastroj(models.Model):
    TYPY_NASTROJU = [
        ('strunne', 'Strunné'),
        ('dechove', 'Dechové'),
        ('klavesove', 'Klávesové'),
        ('bici', 'Bicí'),
        ('jine', 'Jiné'),
    ]

    nazev = models.CharField(max_length=100)
    vyrobce = models.CharField(max_length=100)
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

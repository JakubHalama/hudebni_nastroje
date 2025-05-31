from django.db import migrations, models

def create_manufacturers(apps, schema_editor):
    HudebniNastroj = apps.get_model('nastroje', 'HudebniNastroj')
    Vyrobce = apps.get_model('nastroje', 'Vyrobce')
    
    # Store original manufacturer names
    instruments = HudebniNastroj.objects.all()
    manufacturer_names = {instrument.vyrobce for instrument in instruments if instrument.vyrobce}
    
    # Create manufacturer objects
    manufacturers = {}
    for name in manufacturer_names:
        manufacturers[name] = Vyrobce.objects.create(nazev=name)

def link_manufacturers(apps, schema_editor):
    HudebniNastroj = apps.get_model('nastroje', 'HudebniNastroj')
    Vyrobce = apps.get_model('nastroje', 'Vyrobce')
    
    for instrument in HudebniNastroj.objects.all():
        if instrument.vyrobce:
            manufacturer_name = instrument.vyrobce
            try:
                manufacturer = Vyrobce.objects.get(nazev=manufacturer_name)
                instrument.manufacturer = manufacturer
                instrument.save()
            except Vyrobce.DoesNotExist:
                pass

def reverse_manufacturers(apps, schema_editor):
    Vyrobce = apps.get_model('nastroje', 'Vyrobce')
    Vyrobce.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('nastroje', '0004_remove_hudebninastroj_dostupnost_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vyrobce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100, verbose_name='Název výrobce')),
                ('zeme', models.CharField(blank=True, max_length=100, verbose_name='Země původu')),
                ('popis', models.TextField(blank=True, verbose_name='Popis výrobce')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='vyrobci/')),
                ('web', models.URLField(blank=True, verbose_name='Webové stránky')),
            ],
            options={
                'verbose_name': 'Výrobce',
                'verbose_name_plural': 'Výrobci',
                'ordering': ['nazev'],
            },
        ),
        migrations.RunPython(create_manufacturers),
        migrations.AddField(
            model_name='hudebninastroj',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=models.deletion.CASCADE, related_name='nastroje', to='nastroje.vyrobce', verbose_name='Výrobce'),
        ),
        migrations.RunPython(link_manufacturers),
        migrations.RemoveField(
            model_name='hudebninastroj',
            name='vyrobce',
        ),
        migrations.RenameField(
            model_name='hudebninastroj',
            old_name='manufacturer',
            new_name='vyrobce',
        ),
    ] 
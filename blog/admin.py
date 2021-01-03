from django.contrib import admin
from .models import Cabinets
from .models import Locations
from .models import Persons
from .models import Producers
from .models import Units
from .models import Properties
from .models import Chemicals
from .models import Shelves
from .models import Bottles
from .models import StorageUpdate
from django import forms
from .forms import StorageUpdateForm, ChemicalForm


class BottlesAdmin(admin.ModelAdmin):
    search_fields = ['product_name', 'barcode']
    list_display = ("product_name", "barcode", "shelf", "responsible_person", "registered_date", "bottle_id")
    ordering = ('product_name', '-registered_date')

    class Meta:
        verbose_name_plural = "Bottles"
        ordering = ('product_name', '-registered_date')


class ChemicalsAdmin(admin.ModelAdmin):
    search_fields = ['iupac_name', 'trivial_name', 'formula']
    list_display = ("iupac_name", "trivial_name", "formula", "property", "chemical_id")
    ordering = ('iupac_name',)
    form = ChemicalForm

    class Meta:
        verbose_name_plural = "Chemicals"
        ordering = ('iupac_name',)


class StorageUpdateAdmin(admin.ModelAdmin):
    form = StorageUpdateForm


admin.site.register(StorageUpdate, StorageUpdateAdmin)
admin.site.register(Cabinets)
admin.site.register(Locations)
admin.site.register(Persons)
admin.site.register(Producers)
admin.site.register(Units)
admin.site.register(Properties)
admin.site.register(Chemicals, ChemicalsAdmin)
admin.site.register(Shelves)
admin.site.register(Bottles, BottlesAdmin)

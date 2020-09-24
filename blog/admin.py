from django.contrib import admin
from .models import Bottlefile
from .models import Cabinets
from .models import Locations
from .models import Persons
from .models import Producers
from .models import Units
from .models import Properties
from .models import Chemicals
from .models import Shelves
from .models import Bottles

class BottlesAdmin(admin.ModelAdmin):
    list_display = ("product_name", "barcode", "shelf", "responsible_person", "registered_date", "bottle_id")
    class Meta:
        verbose_name_plural = "Bottles"

class ChemicalsAdmin(admin.ModelAdmin):
    list_display = ("iupac_name", "trivial_name", "formula", "property", "chemical_id")
    class Meta:
        verbose_name_plural = "Chemicals"
        
admin.site.register(Cabinets)
admin.site.register(Locations)
admin.site.register(Persons)
admin.site.register(Producers)
admin.site.register(Units)
admin.site.register(Properties)
admin.site.register(Chemicals, ChemicalsAdmin)
admin.site.register(Shelves)
admin.site.register(Bottles, BottlesAdmin)
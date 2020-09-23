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

admin.site.register(Bottlefile)
admin.site.register(Cabinets)
admin.site.register(Locations)
admin.site.register(Persons)
admin.site.register(Producers)
admin.site.register(Units)
admin.site.register(Properties)
admin.site.register(Chemicals)
admin.site.register(Shelves)
admin.site.register(Bottles)
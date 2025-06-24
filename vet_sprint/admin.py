from django.contrib import admin
from .models import Mascota
from .models import Propietario
from .models import Cita   

# Registra los modelos en el panel de administración de Django
admin.site.register(Propietario)
admin.site.register(Cita)
admin.site.register(Mascota)

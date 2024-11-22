from django.contrib import admin

from django.contrib import admin
from .models.usuario import Usuario
from .models.medida import Medida
from .models.administrador import Administrador

admin.site.register(Usuario)
admin.site.register(Medida)
admin.site.register(Administrador)

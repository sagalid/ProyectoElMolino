# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(TipoPersona)
admin.site.register(DatosPersonales)
admin.site.register(TipoMovil)
admin.site.register(Movil)
admin.site.register(Empresa)
admin.site.register(Convenio)
admin.site.register(Talonario)
admin.site.register(TipoVale)
admin.site.register(PeriodoFacturacion)
admin.site.register(Vale)
admin.site.register(TalonarioVale)

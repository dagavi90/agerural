# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Beneficiarios, Actividades, Funcionarios, Visitas


class VisitaAdmin(admin.ModelAdmin):
    list_display = ('beneficiario', 'fecha_visita', 'funcionario', 'actividad')
    list_filter = ('fecha_visita',)

class BeneficiariosAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'telefono', 'corregimiento', 'vereda')
    search_fields = ('nombres', 'apellidos', 'telefono')

admin.site.register(Visitas, VisitaAdmin)
admin.site.register(Beneficiarios, BeneficiariosAdmin)
admin.site.register(Actividades)
admin.site.register(Funcionarios)
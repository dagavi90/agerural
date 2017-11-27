# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Beneficiarios(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    cedula = models.IntegerField()
    corregimiento = models.CharField(max_length=200)
    vereda = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)


    def __unicode__(self):
        return self.nombres + '  '+self.apellidos

class Actividades(models.Model):
    nombre_actividad=models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre_actividad

class Funcionarios(models.Model):
    nombre_funcionarios=models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre_funcionarios
class Visitas(models.Model):
    beneficiario = models.ForeignKey(Beneficiarios)
    fecha_visita = models.DateField('Fecha de la Visita Técnica')
    diagnostico=models.TextField()
    recomendaciiones=models.TextField()
    actividad=models.ForeignKey(Actividades)
    infraestructura=models.TextField()
    funcionario=models.ForeignKey(Funcionarios)
    hectareas_terreno=models.IntegerField(default=0)
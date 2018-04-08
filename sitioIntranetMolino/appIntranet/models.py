# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxLengthValidator, RegexValidator
from django.utils.timezone import now
import datetime


class TipoPersona(models.Model):
    habilitado = models.BooleanField(default=True)
    tipo_persona = models.CharField(max_length=40)

    def __str__(self):
        return u'%s' % self.tipo_persona


class DatosPersonales(models.Model):
    habilitado = models.BooleanField(default=True)
    tipo_persona = models.ForeignKey(TipoPersona, blank=False, null=False)
    nombre = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    direccion = models.CharField(max_length=150)
    comuna = models.CharField(max_length=150)
    fono_regex = RegexValidator(regex=r'^\+?1?\d{11}$',
                                message="El telefono debe ser ingresado en formato: '+56999999999'. hasta 11 digitos.")
    fono_celular = models.CharField(validators=[fono_regex], max_length=12)
    fono_fijo = models.CharField(validators=[fono_regex], max_length=12)
    correo = models.EmailField(blank=True)
    rut_regex = RegexValidator(regex=r'^\d{1,2}\d{6}[\-][0-9kK]{1}', message="Ingresar el rut con formato '11111111-k'.")
    rut = models.CharField(validators=[rut_regex], max_length=12)
    fecha_nacimiento = models.DateField

    def __str__(self):
        return u'%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)


class TipoMovil(models.Model):
    habilitado = models.BooleanField(default=True)
    tipo_movil = models.CharField(max_length=20)

    def __str__(self):
        return u'%s' % self.tipo_movil


class Movil(models.Model):
    habilitado = models.BooleanField(default=True)
    datos_chofer = models.ForeignKey(DatosPersonales)
    patente = models.CharField(max_length=6)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=50)
    tipo_movil = models.ForeignKey(TipoMovil)
    numero_movil = models.CharField(max_length=4, default='00')
    agno = models.IntegerField(default=2000)
    valor_mes = models.IntegerField(default=1)

    def __str__(self):
        return u'%s' % self.numero_movil


class Empresa(models.Model):
    habilitado = models.BooleanField(default=True)
    rut_regex = RegexValidator(regex=r'^\d{1,2}\.\d{3}\.\d{3}[\-][0-9kK]{1}',
                               message="Ingresar el rut con formato '11.111.111-k'.")
    rut = models.CharField(validators=[rut_regex], max_length=12)
    razon_social = models.CharField(max_length=80)
    rut_representante = models.CharField(validators=[rut_regex], max_length=12)
    nombre_representante = models.CharField(max_length=40)
    direccion = models.CharField(max_length=150)
    comuna = models.CharField(max_length=150)
    fono_regex = RegexValidator(regex=r'^\+?1?\d{11}$',
                                message="El telefono debe ser ingresado en formato: '+56999999999'. hasta 11 digitos.")
    fono_celular = models.CharField(validators=[fono_regex], max_length=12)
    fono_fijo = models.CharField(validators=[fono_regex], max_length=12)
    fono_fax = models.CharField(validators=[fono_regex], max_length=12)
    correo = models.EmailField(blank=True, null=True)

    def __str__(self):
        return u'%s' % self.razon_social


class Convenio(models.Model):
    habilitado = models.BooleanField(default=True)
    nombre_convenio = models.CharField(max_length=50, blank=False, null=False)
    numero_convenio = models.IntegerField
    datos_cliente = models.ForeignKey(DatosPersonales, blank=True, null=True)
    datos_empresa = models.ForeignKey(Empresa, blank=True, null=True)

    def __str__(self):
        return u'%s' % self.nombre_convenio


class Talonario(models.Model):
    habilitado = models.BooleanField(default=True)
    inicio_talonario = models.FloatField
    fin_talonario = models.FloatField
    numero_movil = models.ForeignKey(Movil, blank=True, null=True)
    numero_convenio = models.ForeignKey(Convenio, blank=True, null=True)

    def __str__(self):
        return u'%s %s' % (self.inicio_talonario, self.fin_talonario)


class TipoVale(models.Model):
    habilitado = models.BooleanField(default=True)
    tipo_vale = models.CharField(max_length=15)

    def __str__(self):
        return u'%s' % self.tipo_vale


class PeriodoFacturacion(models.Model):
    habilitado = models.BooleanField(default=False)
    fecha_Inicio = models.DateField(default=now())
    fecha_Fin = models.DateField(default=now())
    detalle = models.TextField(validators=[MaxLengthValidator(300)])

    def __str__(self):
        return u'desde %s al %s' % (self.fecha_Inicio, self.fecha_Fin)

class Vale(models.Model):
    habilitado = models.BooleanField(default=True)
    datos_movil = models.ForeignKey(Movil)
    correlativo = models.FloatField(default=None)
    cliente = models.ForeignKey(Convenio, blank=True, null=True)
    tipo_Vale = models.ForeignKey(TipoVale)
    direccion_origen = models.CharField(max_length=150)
    direccion_destino = models.CharField(max_length=150)
    hora_llamado = models.DateTimeField(default=datetime.datetime.now())
    valor = models.FloatField(default=0)
    observacion = models.TextField(validators=[MaxLengthValidator(300)])
    responsable_ingreso =models.CharField(max_length=100)
    datoPeriodoFacturacion = models.ForeignKey(PeriodoFacturacion)

    def numeroMovil(self):
        return self.datos_movil.numero_movil

    def __str__(self):
        return u'%s %s %s' % (self.correlativo, self.cliente, self.tipo_Vale)


class TalonarioVale(models.Model):
    datos_talonario = models.ForeignKey(Talonario, blank=True, null=True)
    datos_vale = models.ForeignKey(Vale, blank=True, null=True)
    numero_vale = models.IntegerField(default=1)

    def __str__(self):
        return u'%s' % str(self.numero_vale)

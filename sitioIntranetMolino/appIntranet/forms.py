from django import forms
from models import Vale
from bootstrap_datepicker.widgets import DatePicker

__author__ = 'agustinsalas'


class ValeForm(forms.ModelForm):
    valor = forms.IntegerField(widget=forms.TextInput, initial=123)
    correlativo = forms.IntegerField(widget=forms.TextInput, initial=111111)
    correlativo.disabled = True

    hora_llamado = forms.DateField(
        widget=DatePicker(
            options={
                "format": "dd/mm/yyyy",
                "autoclose": True
            }
        )
    )

    class Meta:
        model = Vale
        fields = ('datos_movil',
                  'correlativo',
                  'cliente',
                  'tipo_Vale',
                  'direccion_origen',
                  'direccion_destino',
                  'hora_llamado',
                  'valor',
                  'observacion',
                  'responsable_ingreso',
                  'datoPeriodoFacturacion')

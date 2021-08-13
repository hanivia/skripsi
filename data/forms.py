from django import forms
from django.forms import ModelForm
from .models import *
from appsantri.models import Santri, Pesan

class FormWilayah(ModelForm):
    class Meta:
        model = Wilayah
        fields= '__all__'
        widgets = {        
            'keterangan': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'nama': 'Nama Wilayah',
        }

class FormTahunPelajaran(ModelForm):
    class Meta:
        model = Tahunpelajaran
        fields= '__all__'
        widgets = {
                    'tahun_pelajaran': forms.TextInput(attrs={'class': 'form-control', 
                    'placeholder': 'Tahun Pelajaran',
                    'id':'th'})   
                }

class FormPesan(ModelForm):
    class Meta:
        model = Pesan
        fields= {'status', 'pesan_balasan'}
        widgets = {
            'keterangan': forms.Textarea(attrs={'class': 'form-control'}),
            'pesan_balasan': forms.Textarea(attrs={'class': 'form-control'})
        }

class FormPesandiniyah(ModelForm):
    class Meta:
        model = Pesan
        fields= {'diniyah', 'keterangan'}
        widgets = {     
            'keterangan': forms.Textarea(attrs={'class': 'form-control',
            'placeholder': 'Masukan isi keterangan pesan disini'})      
        }
        labels = {
            'diniyah': 'Dari',
            'keterangan': 'Keterangan',
        }

class FormPesanlembaga(ModelForm):
    class Meta:
        model = Pesan
        fields= {'lembaga', 'keterangan'}
        widgets = {     
            'keterangan': forms.Textarea(attrs={'class': 'form-control',
            'placeholder': 'Masukan isi keterangan pesan disini'})
        }
        labels = {
            'lembaga': 'Dari',
            'keterangan': 'Keterangan',
        }

class FormPesanwilayah(ModelForm):
    class Meta:
        model = Pesan
        fields={'wilayah', 'keterangan'}
        widgets = {
            'keterangan': forms.Textarea(attrs={'class': 'form-control',
            'placeholder': 'Masukan isi keterangan pesan disini'})
        }
        labels = {
            'wilayah': 'Dari',
            'keterangan': 'Keterangan',
        }

class FormSantri(ModelForm):
    class Meta:
        model = Santri
        fields= '__all__'

class SantriSearchForm(forms.ModelForm):
	export_ke_Excel = forms.BooleanField(required=False)
	class Meta:
		model = Santri
		fields = ['diniyah', 'lembaga', 'wilayah', 'tahun_pelajaran']

class SantrisSearchForm(forms.ModelForm):
	export_ke_Excel = forms.BooleanField(required=False)
	class Meta:
		model = Santri
		fields = ['tahun_pelajaran']
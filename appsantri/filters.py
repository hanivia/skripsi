import django_filters
from django_filters import CharFilter
from .models import *


class SantriFilter(django_filters.FilterSet):
    nama = CharFilter(field_name="nama", lookup_expr='icontains')
    nis = CharFilter(field_name="nis", lookup_expr='icontains' )
    nisn = CharFilter(field_name="nisn", lookup_expr='icontains' )
    
    class Meta:
        model = Santri
        fields = ['wilayah', 'lembaga', 'diniyah', 'tahun_pelajaran', 'santri_aktif']
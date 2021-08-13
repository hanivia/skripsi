from django.urls import path
from . import views

urlpatterns = [
    path('', views.santri, name='santri'),
    path('santridiniyah', views.santridiniyah, name='santridiniyah'),
    path('santrilembaga', views.santrilembaga, name='santrilembaga'),
    path('santriwilayah', views.santriwilayah, name='santriwilayah'),
    path('form', views.form_santri, name='form_santri'),
    path('form-edit/<str:pk>', views.edit_santri, name='edit_santri'),
    # path('pdf', views.render_pdf_view, name='pdf'), 
    path('pdf/<str:pk>', views.render_pdf_view, name='pdf'),
    path('pdf_lembaga/<str:pk>', views.render_pdf_lembaga_view, name='pdf_lembaga'),
    path('pdf_diniyah/<str:pk>', views.render_pdf_diniyah_view, name='pdf_diniyah'),
    path('pdf_wilayah/<str:pk>', views.render_pdf_wilayah_view, name='pdf_wilayah'),
    path('grafik', views.grafik, name='grafik_santri'),
    path('grafik2', views.grafik2, name='grafik_santri2'),
    path('grafik3', views.grafik3, name='grafik_santri3'),
    path('export/', views.export, name='export'),
    path('export_santridiniyah/', views.export_santridiniyah, name='export_santridiniyah'),
    path('export_santrilembaga/', views.export_santrilembaga, name='export_santrilembaga'),
    path('export_santriwilayah/', views.export_santriwilayah, name='export_santriwilayah'),
    
]

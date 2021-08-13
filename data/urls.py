from django.urls import path
from . import views
from .views import CustomPasswordChangeView, CustomDiniyahPasswordChangeView, CustomLembagaPasswordChangeView, CustomWilayahPasswordChangeView



urlpatterns = [
    path('', views.beranda, name='beranda'),
    # Wilayah
    path('wilayah/', views.wilayah, name='wilayah'),
    # path('form-wilayah/', views.form_wilayah, name='form_wilayah'),
    path('form-wilayah/', views.FormWilayahView.as_view(), name='form_wilayah'),
    path('edit-wilayah/<str:pk>', views.edit_wilayah, name='edit_wilayah'),
    # Wilayah
    # Lemabaga
    path('lembaga/', views.lembaga, name='lembaga'),
    # path('form-lembaga/', views.form_lembaga, name='form_lembaga'),
    path('form-lembaga/', views.FormLembagaView.as_view(), name='form_lembaga'),
    path('edit-lembaga/<str:pk>', views.edit_lembaga, name='edit_lembaga'),
    # Lemabaga
    # Diniyah
    path('diniyah/', views.diniyah, name='diniyah'),
    path('form-diniyah/', views.FormDiniyahView.as_view(), name='form_diniyah'),
    path('edit-diniyah/<str:pk>', views.edit_diniyah, name='edit_diniyah'),
    # Diniyah
    # tahun ajaran
    path('tahunpelajaran/', views.tahunpelajaran, name='tahunpelajaran'),
    path('form-tahunpelajaran/', views.form_tahunpelajaran, name='form_th'),
    path('edit-tahunpelajaran/<str:pk>', views.edit_tahunpelajaran, name='edit_tahunpelajaran'),
    # tahun ajaran
    # login
    path('login/', views.loginPage, name='login'),
    # logout
    path('logout/', views.logoutPage, name='logout'),
    # change password
    path('password/change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password/changediniyah/', CustomDiniyahPasswordChangeView.as_view(), name='password_changediniyah'),
    path('password/changelembaga/', CustomLembagaPasswordChangeView.as_view(), name='password_changelembaga'),
    path('password/changewilayah/', CustomWilayahPasswordChangeView.as_view(), name='password_changewilayah'),
    # userPage
    path('userdiniyah/', views.userDiniyah, name='user-diniyah'),
    path('userwilayah/', views.userWilayah, name='user-wilayah'),
    path('userlembaga/', views.userLembaga, name='user-lembaga'),
    #catatan
    path('pesan-admin/', views.pesan_admin, name='pesan_admin'),
    path('pesandiniyah/', views.pesandiniyah, name='pesandiniyah'),
    path('pesanlembaga/', views.pesanlembaga, name='pesanlembaga'),
    path('pesanwilayah/', views.pesanwilayah, name='pesanwilayah'),
    path('form-pesandiniyah/', views.form_pesandiniyah, name='form_pesandiniyah'),  
    path('form-pesanlembaga/', views.form_pesanlembaga, name='form_pesanlembaga'), 
    path('form-pesanwilayah/', views.form_pesanwilayah, name='form_pesanwilayah'), 
    path('edit_pesan/<str:pk>', views.edit_pesan, name='edit_pesan'),
    path('hapus_pesan/<str:pk>', views.hapus_pesan, name='hapus_pesan'),

    

    

   
]

from django.db import models
from data.models import *
from django_enumfield import enum


class Santri(models.Model):
    Katerangan=(
        ('Anak Kandung', 'Anak Kandung'),
        ('Anak Angkat', 'Anak Angkat'),
        ('Anak Asuh' , 'Anak Asuh'),
    )
    
    
    nis = models.CharField(max_length=50, blank=True, null=True)
    nisn = models.CharField(max_length=50, blank=True, null=True)
    nik = models.CharField(max_length=50, blank=True, null=True)
    no_kk = models.CharField(max_length=50, blank=True, null=True)
    nama = models.CharField(max_length=200, blank=True, null=True)
    tempat_lahir = models.CharField(max_length=50, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    jenis_kelamin = models.ForeignKey(Jeniskelamin, blank=True, null=True, on_delete=models.SET_NULL)
    agama = models.ForeignKey(Agama, blank=True, null=True, on_delete=models.SET_NULL)
    alamat = models.TextField(max_length=200, blank=True, null=True)
    desa = models.CharField(max_length=30, blank=True, null=True)
    kecamatan = models.CharField(max_length=30, blank=True, null=True)
    kabupaten = models.CharField(max_length=30, blank=True, null=True)
    propinsi = models.CharField(max_length=30, blank=True, null=True)
    hobi = models.ForeignKey(Hobi, blank=True, null=True, on_delete=models.SET_NULL)
    cita_cita = models.ForeignKey(Citacita, blank=True, null=True, on_delete=models.SET_NULL)
    anak_ke = models.PositiveIntegerField(blank=True, null=True)
    jumlah_saudara = models.PositiveIntegerField(blank=True, null=True)
    tanggal_masuk_pesantren =models.DateField(blank=True, null=True)
    status_asal_santri = models.ForeignKey(Statusasalsantri, blank=True, null=True, on_delete=models.SET_NULL)
    sekolah_asal =  models.CharField(max_length=100, blank=True, null=True) 
    alamat_sekolah_asal = models.TextField(max_length=100, blank=True, null=True)
    santri_aktif = models.BooleanField(default=True)
    
    
    wilayah = models.ForeignKey(Wilayah, blank=True, null=True, on_delete=models.SET_NULL)
    lembaga = models.ForeignKey(Lembaga, blank=True, null=True, on_delete=models.SET_NULL)
    diniyah = models.ForeignKey(Diniyah, blank=True, null=True, on_delete=models.SET_NULL)
    tahun_pelajaran = models.ForeignKey(Tahunpelajaran, blank=True, null=True, on_delete=models.SET_NULL)
    foto = models.ImageField(default='fotokosong.gif', upload_to='foto_pics', blank=True)
    
   
    nama_ayah= models.CharField(max_length=200, blank=True, null=True)
    nik_ayah = models.CharField(max_length=50, blank=True, null=True)
    status_hidup_ayah = models.ForeignKey(Statushidupayah, blank=True, null=True, on_delete=models.SET_NULL)
    pendidikan_ayah = models.ForeignKey(Pendidikanayah, blank=True, null=True, on_delete=models.SET_NULL)
    pekerjaan_ayah= models.CharField(max_length=50, blank=True, null=True)
    no_hp_ayah= models.CharField(max_length=20, blank=True, null=True)

  

    nama_ibu= models.CharField(max_length=200, blank=True, null=True)
    nik_ibu = models.CharField(max_length=50, blank=True, null=True)
    status_hidup_ibu = models.ForeignKey(Statushidupibu, blank=True, null=True, on_delete=models.SET_NULL)
    pendidikan_ibu = models.ForeignKey(Pendidikanibu, blank=True, null=True, on_delete=models.SET_NULL)
    pekerjaan_ibu= models.CharField(max_length=50, blank=True, null=True)
    no_hp_ibu= models.CharField(max_length=20, blank=True, null=True)


    nama_wali= models.CharField(max_length=200, blank=True, null=True)
    pendidikan_wali = models.ForeignKey(Pendidikanwali, blank=True, null=True, on_delete=models.SET_NULL)
    pekerjaan_wali= models.CharField(max_length=50, blank=True, null=True)
    no_hp_wali= models.CharField(max_length=20, blank=True, null=True)
    
    penghasilan_orang_tua_atau_wali_perbulan = models.ForeignKey(Penghasilan, blank=True, null=True, on_delete=models.SET_NULL)


    class Meta:
        verbose_name_plural ="Santri"
    def __str__(self):
        return '%s, %s' % (self.id, self.nama)
        # return self.nama 

class PesanStatus(enum.Enum):
    BelumDibalas = 0
    Dibalas = 1

class Pesan(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    lembaga = models.ForeignKey(Lembaga, blank=True, null=True, on_delete=models.SET_NULL)
    diniyah = models.ForeignKey(Diniyah, blank=True, null=True, on_delete=models.SET_NULL)
    wilayah = models.ForeignKey(Wilayah, blank=True, null=True, on_delete=models.SET_NULL)
    keterangan = models.CharField(max_length=500, blank=False, null=True)
    status = enum.EnumField(PesanStatus, default=PesanStatus.BelumDibalas)
    pesan_balasan = models.CharField(max_length=500, blank=False, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural ="Pesan"
    def __str__(self):
        return '%s, %s, %s' % (self.lembaga, self.diniyah, self.wilayah)
        # return self.nama 




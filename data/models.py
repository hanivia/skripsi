from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Wilayah(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=False, null=True)
    keterangan = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural ="Wilayah"
    def __str__(self):
        return self.nama 
        # return '%s, %s' % (self.id, self.nama)
    
class Tahunpelajaran(models.Model):
    tahun_pelajaran = models.CharField(max_length=50, blank=False, null=True)
   
    class Meta:
        verbose_name_plural ="Tahunpelajaran"
    def __str__(self):
        return self.tahun_pelajaran 
        # return '%s, %s' % (self.id, self.tahun_pelajaran)

class Lembaga(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Lembaga"
    def __str__(self):
        return self.nama 
        # return '%s, %s' % (self.id, self.nama)

class Jeniskelamin(models.Model):
    jenis = models.CharField(max_length=50, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Jeniskelamin"
    def __str__(self):
        return self.jenis 
        # return '%s, %s' % (self.id, self.jenis)

class Diniyah(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Diniyah"
    def __str__(self):
        return self.nama
        # return '%s, %s' % (self.id, self.nama)

class Hobi(models.Model):
    hobi = models.CharField(max_length=100, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Hobi"
    def __str__(self):
        return self.hobi 
        # return '%s, %s' % (self.id, self.hobi)

class Agama(models.Model):
    agama = models.CharField(max_length=100, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Agama"
    def __str__(self):
        return self.agama 
        # return '%s, %s' % (self.id, self.agama)    

class Citacita(models.Model):
    cita = models.CharField(max_length=100, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="CItacita"
    def __str__(self):
        return self.cita
        # return '%s, %s' % (self.id, self.cita)

class Statusasalsantri(models.Model):
    status_asal_santri = models.CharField(max_length=200, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Statusasalsantri"
    def __str__(self):
        return self.status_asal_santri
        # return '%s, %s' % (self.id, self.statusasalsantri)

class Statushidupibu(models.Model):
    status_hidup_ibu = models.CharField(max_length=100, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Statushidupibu"
    def __str__(self):
        return self.status_hidup_ibu
        # return '%s, %s' % (self.id, self.statushidupibu)

class Statushidupayah(models.Model):
    status_hidup_ayah = models.CharField(max_length=100, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Statushidupayah"
    def __str__(self):
        return self.status_hidup_ayah
        # return '%s, %s' % (self.id, self.statushidupayah)

class Pendidikanayah(models.Model):
    pendidikan_ayah = models.CharField(max_length=100, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Pendidikanayah"
    def __str__(self):
        return self.pendidikan_ayah
        # return '%s, %s' % (self.id, self.pendidikanayah)

class Pendidikanibu(models.Model):
    pendidikan_ibu = models.CharField(max_length=100, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Pendidikanibu"
    def __str__(self):
        return self.pendidikan_ibu
        # return '%s, %s' % (self.id, self.pendidikanibu)

class Pendidikanwali(models.Model):
    pendidikan_wali = models.CharField(max_length=100, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Pendidikanwali"
    def __str__(self):
        return self.pendidikan_wali
        # return '%s, %s' % (self.id, self.pendidikanwali)

class Penghasilan(models.Model):
    penghasilan = models.CharField(max_length=100, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Penghasilan"
    def __str__(self):
        return self.penghasilan
        # return '%s, %s' % (self.id, self.penghasilan)
        
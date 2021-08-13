from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.
from .forms import FormWilayah, FormTahunPelajaran, FormPesan, FormPesandiniyah, FormPesanlembaga, FormPesanwilayah
from .models import *
from appsantri.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.views.generic import View
from django.views.generic import ListView
from validate_email import validate_email
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import tolakhalaman_ini, pilihan_login, ijinkan_pengguna

@login_required(login_url='login')
@pilihan_login
def beranda(request):
    list_santri = Santri.objects.all()
    list_wilayah = Wilayah.objects.all()
    list_lembaga = Lembaga.objects.all()
    list_diniyah = Diniyah.objects.all()
    total_santri = list_santri.count()
    total_santri_putra = list_santri.filter(jenis_kelamin_id = '1').count()
    total_santri_putri = list_santri.filter(jenis_kelamin_id = '2').count()
    total_wilayah = list_wilayah.count()
    total_lembaga = list_lembaga.count()
    total_diniyah = list_diniyah.count()

    context={
        'judul': 'Halaman Beranda',
        'menu': 'beranda',
        'total_data_santri': total_santri,
        'total_data_santri_putra': total_santri_putra,
        'total_data_santri_putri': total_santri_putri,
        'total_data_wilayah': total_wilayah,
        'total_data_lembaga': total_lembaga,
        'total_data_diniyah': total_diniyah,
    }
    return render(request, 'data/beranda.html', context)


# Wilayah
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def wilayah(request):
    list_wilayah = Wilayah.objects.all()
    context={
        'judul': 'Halaman Wilayah',
        'menu': 'wilayah',
        'list': list_wilayah,
    }
    return render(request, 'data/wilayah.html', context)


class FormWilayahView(View):
    def get(self, request):
        context={
        'judul': 'Form Wilayah',
        'menu': 'wilayah',
            
        }
        return render(request, 'data/form_wilayah.html', context)
   
    def post(self, request):
        context={
        'judul': 'Form Wilayah',
        'menu': 'wilayah',
        'has_error': False,
        'data': request.POST
        }
       
        nama = request.POST.get('nama')
        username = request.POST.get('username')
        password = request.POST.get('pass')
        password2 = request.POST.get('pass2')
        if not nama:
            messages.add_message(request, messages.ERROR,'Maaf nama masih kosong')
            context['has_error'] = True
        if len(password) < 6:
           messages.add_message(request, messages.ERROR,'Password minimal harus 6 karekter')
           context['has_error'] = True
        if password!=password2:
           messages.add_message(request, messages.ERROR,'Password tidak sama')
           context['has_error'] = True
        try:
            if User.objects.get(username=username):
                messages.add_message(
                    request, messages.ERROR, 'Username Sudah ada')
                context['has_error'] = True

        except Exception as identifier:
            pass
 
        if context['has_error']:
            return render(request, 'data/form_wilayah.html', context, status=400)
        user = User.objects.create_user(username=username)
        user.set_password(password)
        user.is_active = True
        user.save()
        
        wilayah_obj = Wilayah.objects.create(user = user, nama = nama)
        wilayah_obj.save()
        
        akses_wilayah = Group.objects.get(name='wilayah')
        user.groups.add(akses_wilayah)       

        messages.success(request,'Data wilayah berhasil tersimpan.')
        return redirect('wilayah')


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def edit_wilayah(request, pk):
    wilayahdata = Wilayah.objects.get(id=pk)
    if request.method == 'POST':
        nama = request.POST.get('nama')
        if not nama:
            messages.add_message(request, messages.ERROR,'Maaf nama masih kosong')
            return redirect('edit_wilayah')
        wilayahdata.nama = nama
        wilayahdata.save()
        messages.success(request,'Data wilayah berhasil teredit.')
        return redirect('wilayah')
        
    context={
        'judul': 'Edit Wilayah',
        'menu': 'wilayah',
        'r': wilayahdata
    }
    return render(request, 'data/form_edit_wilayah.html', context)
# Wilayah

# Lembaga
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def lembaga(request):
    list_lembaga = Lembaga.objects.all()
    context={
        'judul': 'Halaman Lembaga',
        'menu': 'lembaga',
        'list': list_lembaga,
    }
    return render(request, 'data/lembaga.html', context)
    return render(request, 'data/jumlah.html', context)

class FormLembagaView(View):
    def get(self, request):
        context={
        'judul': 'Form Lembaga',
        'menu': 'lembaga',
        }
        return render(request, 'data/form_lembaga.html', context)
   
    def post(self, request):
        context={
        'judul': 'Form Lembaga',
        'menu': 'lembaga',
        'has_error': False,
        'data': request.POST
        }
       
        nama = request.POST.get('nama')
        username = request.POST.get('username')
        password = request.POST.get('pass')
        password2 = request.POST.get('pass2')
        if not nama:
            messages.add_message(request, messages.ERROR,'Maaf nama masih kosong')
            context['has_error'] = True
        if len(password) < 6:
           messages.add_message(request, messages.ERROR,'Password minimal harus 6 karekter')
           context['has_error'] = True
        if password!=password2:
           messages.add_message(request, messages.ERROR,'Password tidak sama')
           context['has_error'] = True
        try:
            if User.objects.get(username=username):
                messages.add_message(
                    request, messages.ERROR, 'Username Sudah ada')
                context['has_error'] = True

        except Exception as identifier:
            pass
 
        if context['has_error']:
            return render(request, 'data/form_lembaga.html', context, status=400)
        user = User.objects.create_user(username=username)
        user.set_password(password)
        user.is_active = True
        user.save()
        
        lembaga_obj = Lembaga.objects.create(user = user, nama = nama)
        lembaga_obj.save()
        
        akses_lembaga = Group.objects.get(name='lembaga')
        user.groups.add(akses_lembaga)

        messages.success(request,'Data lembaga berhasil tersimpan.')
        return redirect('lembaga')
        

@ijinkan_pengguna(yang_diizinkan=['admin'])
def edit_lembaga(request, pk):
    lembagadata = Lembaga.objects.get(id=pk)
    if request.method == 'POST':
        nama = request.POST.get('nama')
        if not nama:
            messages.add_message(request, messages.ERROR,'Maaf nama masih kosong')
            return redirect('edit_lembaga')
        lembagadata.nama = nama
        lembagadata.save()
        messages.success(request,'Data lembaga berhasil teredit.')
        return redirect('lembaga')
       
    context={
        'judul': 'Edit Lembaga',
        'menu': 'lembaga',
        'r': lembagadata
    }
    return render(request, 'data/form_edit_lembaga.html', context)
# Lembaga


# TahunPelajaran
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def tahunpelajaran(request):
    list_th = Tahunpelajaran.objects.all()
    context={
        'judul': 'Halaman Tahun Pelajaran',
        'menu': 'tahunpelajaran',
        'list': list_th
    }
    return render(request, 'data/tahunpelajaran.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def form_tahunpelajaran(request):
    form_th = FormTahunPelajaran()
    if request.method == 'POST':
        formsimpan = FormTahunPelajaran(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('tahunpelajaran')
    context={
        'judul': 'Form Tahun Pelajaran',
        'menu': 'tahunpelajaran',
        'form': form_th
    }
    return render(request, 'data/form_th.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def edit_tahunpelajaran(request,pk):
    thdata = Tahunpelajaran.objects.get(id=pk)
    form_th = FormTahunPelajaran(instance=thdata)
    if request.method == 'POST':
        formsimpan = FormTahunPelajaran(request.POST, instance=thdata)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('tahunpelajaran')
    context={
        'judul': 'Form Tahun Pelajaran',
         'menu': 'tahunpelajaran',
        'form': form_th
    }
    return render(request, 'data/form_th.html', context)
#TahunPelajaran


# Diniyah
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def diniyah(request):
    list_diniyah = Diniyah.objects.all()
    context={
        'judul': 'Halaman Diniyah',
        'menu': 'diniyah',
        'list': list_diniyah,
    }
    return render(request, 'data/diniyah.html', context)
    return render(request, 'data/beranda.html', context)

class FormDiniyahView(View):
    def get(self, request):
        context={
        'judul': 'Form Diniyah',
        'menu': 'diniyah',
       
        }
        return render(request, 'data/form_diniyah.html', context)
   
    def post(self, request):
        context={
        'judul': 'Form Diniyah',
        'menu': 'diniyah',
        'has_error': False,
        'data': request.POST
        }
       
        nama = request.POST.get('nama')
        # email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('pass')
        password2 = request.POST.get('pass2')
        if not nama:
            messages.add_message(request, messages.ERROR,'Maaf nama masih kosong')
            context['has_error'] = True
        # if not validate_email(email):
        #    messages.add_message(request, messages.ERROR,'Maaf Email Anda tidak valid')
        #    context['has_error'] = True
        if len(password) < 6:
           messages.add_message(request, messages.ERROR,'Password minimal harus 6 karekter')
           context['has_error'] = True
        if password!=password2:
           messages.add_message(request, messages.ERROR,'Password tidak sama')
           context['has_error'] = True
        try:
            if User.objects.get(username=username):
                messages.add_message(
                    request, messages.ERROR, 'Username Sudah ada')
                context['has_error'] = True

        except Exception as identifier:
            pass
        # try:
        #     if User.objects.get(email=email):
        #         messages.add_message(request, messages.ERROR, 'Email Sudah ada')
        #         context['has_error'] = True

        # except Exception as identifier:
        #     pass
 
        if context['has_error']:
            return render(request, 'data/form_diniyah.html', context, status=400)
        user = User.objects.create_user(username=username)
        # user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.is_active = True
        user.save()
        
        diniyah_obj = Diniyah.objects.create(user = user, nama = nama)
        diniyah_obj.save()
        
        akses_diniyah = Group.objects.get(name='diniyah')
        user.groups.add(akses_diniyah)

        messages.success(request,'Data diniyah berhasil tersimpan.')
        return redirect('diniyah')


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def edit_diniyah(request, pk):
    diniyahdata = Diniyah.objects.get(id=pk)
    if request.method == 'POST':
        nama = request.POST.get('nama')
        if not nama:
            messages.add_message(request, messages.ERROR,'Maaf nama masih kosong')
            return redirect('edit_diniyah')
        diniyahdata.nama = nama
        diniyahdata.save()
        messages.success(request,'Data diniyah berhasil teredit.')
        return redirect('diniyah')    
    context={
        'judul': 'Edit Diniyah',
        'menu': 'diniyah',
        'r': diniyahdata
    }
    return render(request, 'data/form_edit_diniyah.html', context)
# Diniyah



#fungsi loginPage
@tolakhalaman_ini
def loginPage (request):
    if request.user.is_authenticated:
        return render(request, 'data/beranda.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cocokan = authenticate(request, username=username, password=password )
        if cocokan is not None:
            login(request, cocokan)
            return redirect('beranda')
        else:
            msg = 'Failed Login! Pastikan username dan pasword benar'
            form = AuthenticationForm(request.POST)
            return render(request, 'data/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'data/login.html', {'form': form})
  
    context = {
        'judul': 'Halaman Login',
        'menu': 'login',
        'tampillogin' : formlogin
    }
    return render(request, 'data/login.html', context)


# fungsi logoutPage
def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
# @pilihan_login
@ijinkan_pengguna(yang_diizinkan=['diniyah'])
def userDiniyah(request):
    list_santridiniyah = Santri.objects.all().filter(diniyah=request.user.diniyah) 
    total_santridiniyah = list_santridiniyah.count()
    total_santridiniyah_putra = list_santridiniyah.filter(jenis_kelamin_id = '1').count()
    total_santridiniyah_putri = list_santridiniyah.filter(jenis_kelamin_id = '2').count()
    context={
        'judul': 'Halaman Beranda',
        'menu': 'userdiniyah',
        'total_data_santridiiyah': total_santridiniyah,
        'total_data_santridiniyah_putra': total_santridiniyah_putra,
        'total_data_santridiniyah_putri': total_santridiniyah_putri,
        
    }
    return render(request, 'data/userdiniyah.html', context)
   

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['wilayah'])
def userWilayah(request):
    list_santriwilayah = Santri.objects.all().filter(wilayah=request.user.wilayah) 
    total_santriwilayah = list_santriwilayah.count()
    total_santriwilayah_putra = list_santriwilayah.filter(jenis_kelamin_id = '1').count()
    total_santriwilayah_putri = list_santriwilayah.filter(jenis_kelamin_id = '2').count()
    context={
        'judul': 'Halaman Beranda',
        'menu': 'userwilayah',
        'total_data_santriwilayah': total_santriwilayah,
        'total_data_santriwilayah_putra': total_santriwilayah_putra,
        'total_data_santriwilayah_putri': total_santriwilayah_putri,
    }
    return render(request, 'data/userwilayah.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['lembaga'])
def userLembaga(request):
    list_santrilembaga = Santri.objects.all().filter(lembaga=request.user.lembaga) 
    total_santrilembaga = list_santrilembaga.count()
    total_santrilembaga_putra = list_santrilembaga.filter(jenis_kelamin_id = '1').count()
    total_santrilembaga_putri = list_santrilembaga.filter(jenis_kelamin_id = '2').count()
    
    context={
        'judul': 'Halaman Beranda',
        'menu': 'userlembaga',
        'total_data_santrilembaga': total_santrilembaga,
        'total_data_santrilembaga_putra': total_santrilembaga_putra,
        'total_data_santrilembaga_putri': total_santrilembaga_putri,
    }
    return render(request, 'data/userlembaga.html', context)
   

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['diniyah'])
def pesandiniyah(request):
    list_pesan = Pesan.objects.all().filter(diniyah=request.user.diniyah)
    context={
        'judul': 'Halaman Pesan',
        'menu': 'pesanadmindiniyah',
        'list': list_pesan,
    }
    return render(request, 'data/pesandiniyah.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['lembaga'])
def pesanlembaga(request):
    list_pesan = Pesan.objects.all().filter(lembaga=request.user.lembaga)
    context={
        'judul': 'Halaman Pesan',
        'menu': 'pesanadminlembaga',
        'list': list_pesan,
    }
    return render(request, 'data/pesanlembaga.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['wilayah'])
def pesanwilayah(request):
    list_pesan = Pesan.objects.all().filter(wilayah=request.user.wilayah)
    context={
        'judul': 'Halaman Pesan',
        'menu': 'pesanadminwilayah',
        'list': list_pesan,
    }
    return render(request, 'data/pesanwilayah.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def pesan_admin(request):
    list_pesan = Pesan.objects.all()
    # pagination
    paginated_pesan = Paginator(list_pesan, 10)
    page_number = request.GET.get('page')
    pesan_page_obj = paginated_pesan.get_page(page_number)

    context={
        'judul': 'Halaman Pesan',
        'menu': 'pesan',
        'list': list_pesan,
        'pesan_page_obj': pesan_page_obj,
    }
    return render(request, 'data/pesan_admin.html', context)


@login_required(login_url='login') 
@ijinkan_pengguna(yang_diizinkan=['admin'])   
def edit_pesan(request, pk):
    pesan = Pesan.objects.get(id=pk)
    form_edit_pesan = FormPesan(instance=pesan)
    if request.method == 'POST':
        formsimpan = FormPesan(request.POST, request.FILES, instance=pesan)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('pesan_admin')
    context={
        'judul': 'Halaman Form Pesan',
        'form': form_edit_pesan,
    }
    return render(request, 'data/form_edit_pesan.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['diniyah'])
def form_pesandiniyah(request):
    form_pesan = FormPesandiniyah()
    if request.method == 'POST':
        formsimpan = FormPesandiniyah(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('pesandiniyah')
    context={
        'judul': 'Form Pesan',
        'menu': 'pesandiniyah',
        'form': form_pesan
    }
    return render(request, 'data/form_pesandiniyah.html', context)




@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['lembaga'])
def form_pesanlembaga(request):
    form_pesan = FormPesanlembaga()
    if request.method == 'POST':
        formsimpan = FormPesanlembaga(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('pesanlembaga')
    context={
        'judul': 'Form Pesan',
        'menu': 'pesanlembaga',
        'form': form_pesan
    }
    return render(request, 'data/form_pesanlembaga.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['wilayah'])
def form_pesanwilayah(request):
    form_pesan = FormPesanwilayah()
    if request.method == 'POST':
        formsimpan = FormPesanwilayah(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('pesanwilayah')
    context={
        'judul': 'Form Pesan',
        'menu': 'pesanwilayah',
        'form': form_pesan
    }
    return render(request, 'data/form_pesanwilayah.html', context)
    
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def hapus_pesan(request, pk):
    pesanhapus = Pesan.objects.get(id=pk)
    if request.method == 'POST':
        pesanhapus.delete()
        return redirect('pesan_admin')

    context = {
        'judul': 'Hapus Pesan',
        'pesanhapus' : pesanhapus, 
    }
    return render(request, 'data/pesan_hapus.html', context)

# change passord
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'data/password_change.html'
    success_url = reverse_lazy('beranda')

    def form_valid(self, form):
        messages.success(self.request, 'Password berhasil diubah, jaga baik-baik ya passwordnya')
        return super().form_valid(form)

class CustomDiniyahPasswordChangeView(PasswordChangeView):
    template_name = 'data/password_changediniyah.html'
    success_url = reverse_lazy('user-diniyah')

    def form_valid(self, form):
        messages.success(self.request, 'Password berhasil diubah, jaga baik-baik ya passwordnya')
        return super().form_valid(form)

class CustomLembagaPasswordChangeView(PasswordChangeView):
    template_name = 'data/password_changelembaga.html'
    success_url = reverse_lazy('user-lembaga')

    def form_valid(self, form):
        messages.success(self.request, 'Password berhasil diubah, jaga baik-baik ya passwordnya')
        return super().form_valid(form)

class CustomWilayahPasswordChangeView(PasswordChangeView):
    template_name = 'data/password_changewilayah.html'
    success_url = reverse_lazy('user-wilayah')

    def form_valid(self, form):
        messages.success(self.request, 'Password berhasil diubah, jaga baik-baik ya passwordnya')
        return super().form_valid(form)



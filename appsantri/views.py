from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from data.forms import FormSantri, SantriSearchForm, SantrisSearchForm
import xlwt
from .models import Santri
from data.models import Lembaga
from data.models import Diniyah
from django.db.models import Count
from .filters import SantriFilter
from django.contrib.auth.decorators import login_required
from data.decorators import ijinkan_pengguna

from django.db.models import Q


# PDF Library
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# PDF Library

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['diniyah'])
def santridiniyah(request):
    list_santri = Santri.objects.all().filter(diniyah=request.user.diniyah)  
    filter_santri = SantriFilter(request.GET, queryset=list_santri)
    list_santri=filter_santri.qs
    # pagination
    paginated_filter_santri = Paginator(filter_santri.qs, 2)
    page_number = request.GET.get('page')
    santri_page_obj = paginated_filter_santri.get_page(page_number)

    context={
        'judul': 'Halaman Santri',
        'menu': 'santridiniyah', 
        'list': list_santri,
        'filter_data_santri':filter_santri,
        'santri_page_obj':santri_page_obj,
    }
    
    return render(request, 'appsantri/santridiniyah.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['lembaga'])
def santrilembaga(request):
    list_santri = Santri.objects.all().filter(lembaga=request.user.lembaga)  
    filter_santri = SantriFilter(request.GET, queryset=list_santri)
    list_santri=filter_santri.qs
    # pagination
    paginated_filter_santri = Paginator(filter_santri.qs, 2)
    page_number = request.GET.get('page')
    santri_page_obj = paginated_filter_santri.get_page(page_number)
    
    context={
        'judul': 'Halaman Santri',
        'menu': 'santrilembaga',
        'list': list_santri,
        'filter_data_santri':filter_santri,
        'santri_page_obj':santri_page_obj,
    }
    return render(request, 'appsantri/santrilembaga.html', context)
    

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['wilayah'])
def santriwilayah(request):
    list_santri = Santri.objects.all().filter(wilayah=request.user.wilayah)  
    filter_santri = SantriFilter(request.GET, queryset=list_santri)
    list_santri=filter_santri.qs
    # pagination
    paginated_filter_santri = Paginator(filter_santri.qs, 10)
    page_number = request.GET.get('page')
    santri_page_obj = paginated_filter_santri.get_page(page_number)

    context={
        'judul': 'Halaman Santri',
        'menu': 'santriwilayah', 
        'list': list_santri,
        'filter_data_santri':filter_santri,
        'santri_page_obj':santri_page_obj,
    }
    
    return render(request, 'appsantri/santriwilayah.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def santri(request):
    list_santri = Santri.objects.all()
    filter_santri = SantriFilter(request.GET, queryset=list_santri)
    list_santri_cari=filter_santri.qs
    # pagination
    paginated_filter_santri = Paginator(filter_santri.qs, 2)
    page_number = request.GET.get('page')
    santri_page_obj = paginated_filter_santri.get_page(page_number)

    
    data_csv = request.POST.get('csv')

    
    if request.method == 'POST':
        if data_csv == 'on':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="santri.csv"'
            writer = csv.writer(response) 
            writer.writerow(['NIS', 'NAMA']) 
            instance = santri_page_obj
            for row in instance: 
                writer.writerow([row.nama, row.nis]) 
            return response
        
    
    context={
        'judul': 'Halaman Santri',
        'menu': 'santri', 
        'list': list_santri,
        'filter_data_santri':filter_santri,
        'santri_page_obj':santri_page_obj,  
    }
 
    return render(request, 'appsantri/santri.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def export(request):
    header = 'Halaman Export Data'
    queryset = Santri.objects.all()
    form = SantriSearchForm(request.POST or None)
    context = {
        "judul": header,
        "queryset": queryset,
        "menu": "export",
        "form": form,
    }
    if request.method == 'POST':
        lembaga = form['lembaga'].value()
        diniyah = form['diniyah'].value()
        wilayah = form['wilayah'].value()
        tahun_pelajaran = form['tahun_pelajaran'].value()
        # queryset = Santri.objects.filter(nama__icontains=form['nama'].value())
        if (lembaga != ''):
            queryset = queryset.filter(lembaga_id=lembaga)
        if (diniyah != ''):
            queryset = queryset.filter(diniyah_id=diniyah)
        if (wilayah != ''):
            queryset = queryset.filter(wilayah_id=wilayah)
        if (tahun_pelajaran != ''):
            queryset = queryset.filter(tahun_pelajaran_id=tahun_pelajaran)

        
        if form['export_ke_Excel'].value() == True:
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="Data santri.xls"'
        
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Santri')
        
            # Sheet header, first row
            row_num = 0
        
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
        
            columns = ['NIS', 'NISN', 'NIK', 'NO KK', 'NAMA', 'TEMPAT LAHIR', 'TANGGAL LAHIR', 'JENIS KELAMIN', 'AGAMA', 'ALAMAT', 'KECAMATAN', 'KABUPATEN', 'PROPINSI', 'HOBI', 'CITA CITA', 'ANAK KE', 'JUMLAH SAUDARA', 'TGL MASUK PESANTREN', 'STATUS ASAL SANTRI', 'SEKOLAH ASAL', 'ALAMAT SEKOLAH ASAL',
                        'WILAYAH', 'LEMBAGA', 'DINIYAH', 'TAHUN PELAJARAN', 
                        'NAMA AYAH', 'STATUS HIDUP AYAH', 'PENDIDIKAN AYAH', 'PEKERJAAN AYAH', 'NO HP AYAH',
                        'NAMA IBU', 'STATUS HIDUP IBU', 'PENDIDIKAN IBU', 'PEKERJAAN IBU', 'NO HP IBU',
                        'NAMA WALI', 'PENDIDIKAN WALI', 'PEKERJAAN WALI', 'NO HP WALI', 'PENGHASILAN ORANG TUA ATAU WALI PERBULAN' ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
        
            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            
            
            rows = queryset.values_list('nis', 'nisn', 'nik', 'no_kk', 'nama', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'agama', 'alamat', 'kecamatan', 'kabupaten', 'propinsi', 'hobi', 'cita_cita', 'anak_ke', 'jumlah_saudara', 'tanggal_masuk_pesantren', 'status_asal_santri', 'sekolah_asal', 'alamat_sekolah_asal',
                        'wilayah', 'lembaga', 'diniyah', 'tahun_pelajaran', 
                        'nama_ayah', 'status_hidup_ayah', 'pendidikan_ayah', 'pekerjaan_ayah', 'no_hp_ayah',
                        'nama_ibu', 'status_hidup_ibu', 'pendidikan_ibu', 'pekerjaan_ibu', 'no_hp_ibu',
                        'nama_wali', 'pendidikan_wali', 'pekerjaan_wali', 'no_hp_wali', 'penghasilan_orang_tua_atau_wali_perbulan' )
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        
            wb.save(response)
            return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
            "menu": "export",
        }
		
    return render(request, 'appsantri/export.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['diniyah'])
def export_santridiniyah(request):
    header = 'Halaman Export Data'
    queryset = Santri.objects.all()
    form = SantrisSearchForm(request.POST or None)
    context = {
        "judul": header,
        "queryset": queryset,
        "menu": "export_santridiniyah",
        "form": form,
    }
    if request.method == 'POST':
        tahun_pelajaran = form['tahun_pelajaran'].value()
        # queryset = Santri.objects.filter(nama__icontains=form['nama'].value())
        if (tahun_pelajaran != ''):
            queryset = Santri.objects.filter(tahun_pelajaran_id=tahun_pelajaran)

        if form['export_ke_Excel'].value() == True:
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="santri.xls"'
        
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Santri')
        
            # Sheet header, first row
            row_num = 0
        
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
        
            columns = ['NIS', 'NISN', 'NIK', 'NO KK', 'NAMA', 'TEMPAT LAHIR', 'TANGGAL LAHIR', 'JENIS KELAMIN', 'AGAMA', 'ALAMAT', 'KECAMATAN', 'KABUPATEN', 'PROPINSI', 'HOBI', 'CITA CITA', 'ANAK KE', 'JUMLAH SAUDARA', 'TGL MASUK PESANTREN', 'STATUS ASAL SANTRI', 'SEKOLAH ASAL', 'ALAMAT SEKOLAH ASAL',
                        'WILAYAH', 'LEMBAGA', 'DINIYAH', 'TAHUN PELAJARAN', 
                        'NAMA AYAH', 'STATUS HIDUP AYAH', 'PENDIDIKAN AYAH', 'PEKERJAAN AYAH', 'NO HP AYAH',
                        'NAMA IBU', 'STATUS HIDUP IBU', 'PENDIDIKAN IBU', 'PEKERJAAN IBU', 'NO HP IBU',
                        'NAMA WALI', 'PENDIDIKAN WALI', 'PEKERJAAN WALI', 'NO HP WALI', 'PENGHASILAN ORANG TUA ATAU WALI PERBULAN' ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
        
            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            
            
            rows = queryset.filter(diniyah=request.user.diniyah).values_list('nis', 'nisn', 'nik', 'no_kk', 'nama', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'agama', 'alamat', 'kecamatan', 'kabupaten', 'propinsi', 'hobi', 'cita_cita', 'anak_ke', 'jumlah_saudara', 'tanggal_masuk_pesantren', 'status_asal_santri', 'sekolah_asal', 'alamat_sekolah_asal',
                        'wilayah', 'lembaga', 'diniyah', 'tahun_pelajaran',
                        'nama_ayah', 'status_hidup_ayah', 'pendidikan_ayah', 'pekerjaan_ayah', 'no_hp_ayah',
                        'nama_ibu', 'status_hidup_ibu', 'pendidikan_ibu', 'pekerjaan_ibu', 'no_hp_ibu',
                        'nama_wali', 'pendidikan_wali', 'pekerjaan_wali', 'no_hp_wali', 'penghasilan_orang_tua_atau_wali_perbulan' )
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        
            wb.save(response)
            return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
            "menu": "export_santridiniyah",
        }
    return render(request, 'appsantri/export_santridiniyah.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['lembaga'])
def export_santrilembaga(request):
    header = 'Halaman Export Data'
    queryset = Santri.objects.all()
    form = SantrisSearchForm(request.POST or None)
    context = {
        "judul": header,
        "queryset": queryset,
        "menu": "export_santrilembaga",
        "form": form,
    }
    if request.method == 'POST':
        tahun_pelajaran = form['tahun_pelajaran'].value()
        if (tahun_pelajaran != ''):
            queryset = Santri.objects.filter(tahun_pelajaran_id=tahun_pelajaran)

        if form['export_ke_Excel'].value() == True:
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="santri.xls"'
        
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Santri')
        
            # Sheet header, first row
            row_num = 0
        
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
        
            columns = ['NIS', 'NISN', 'NIK', 'NO KK', 'NAMA', 'TEMPAT LAHIR', 'TANGGAL LAHIR', 'JENIS KELAMIN', 'AGAMA', 'ALAMAT', 'KECAMATAN', 'KABUPATEN', 'PROPINSI', 'HOBI', 'CITA CITA', 'ANAK KE', 'JUMLAH SAUDARA', 'TGL MASUK PESANTREN', 'STATUS ASAL SANTRI', 'SEKOLAH ASAL', 'ALAMAT SEKOLAH ASAL',
                        'WILAYAH', 'LEMBAGA', 'DINIYAH', 'TAHUN PELAJARAN', 
                        'NAMA AYAH', 'STATUS HIDUP AYAH', 'PENDIDIKAN AYAH', 'PEKERJAAN AYAH', 'NO HP AYAH',
                        'NAMA IBU', 'STATUS HIDUP IBU', 'PENDIDIKAN IBU', 'PEKERJAAN IBU', 'NO HP IBU',
                        'NAMA WALI', 'PENDIDIKAN WALI', 'PEKERJAAN WALI', 'NO HP WALI', 'PENGHASILAN ORANG TUA ATAU WALI PERBULAN' ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
        
            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            
            
            rows = queryset.filter(lembaga=request.user.lembaga).values_list('nis', 'nisn', 'nik', 'no_kk', 'nama', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'agama', 'alamat', 'kecamatan', 'kabupaten', 'propinsi', 'hobi', 'cita_cita', 'anak_ke', 'jumlah_saudara', 'tanggal_masuk_pesantren', 'status_asal_santri', 'sekolah_asal', 'alamat_sekolah_asal',
                        'wilayah', 'lembaga', 'diniyah', 'tahun_pelajaran',
                        'nama_ayah', 'status_hidup_ayah', 'pendidikan_ayah', 'pekerjaan_ayah', 'no_hp_ayah',
                        'nama_ibu', 'status_hidup_ibu', 'pendidikan_ibu', 'pekerjaan_ibu', 'no_hp_ibu',
                        'nama_wali', 'pendidikan_wali', 'pekerjaan_wali', 'no_hp_wali', 'penghasilan_orang_tua_atau_wali_perbulan' )
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        
            wb.save(response)
            return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
            "menu": "export_santrilembaga",
        }
    return render(request, 'appsantri/export_santrilembaga.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['wilayah'])
def export_santriwilayah(request):
    header = 'Halaman Export Data'
    queryset = Santri.objects.all()
    form = SantrisSearchForm(request.POST or None)
    context = {
        "judul": header,
        "queryset": queryset,
        "menu": "export_santriwilayah",
        "form": form,
    }
    if request.method == 'POST':
        tahun_pelajaran = form['tahun_pelajaran'].value()
        if (tahun_pelajaran != ''):
            queryset = Santri.objects.filter(tahun_pelajaran_id=tahun_pelajaran)

        if form['export_ke_Excel'].value() == True:
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="santri.xls"'
        
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Santri')
        
            # Sheet header, first row
            row_num = 0
        
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
        
            columns = ['NIS', 'NISN', 'NIK', 'NO KK', 'NAMA', 'TEMPAT LAHIR', 'TANGGAL LAHIR', 'JENIS KELAMIN', 'AGAMA', 'ALAMAT', 'KECAMATAN', 'KABUPATEN', 'PROPINSI', 'HOBI', 'CITA CITA', 'ANAK KE', 'JUMLAH SAUDARA', 'TGL MASUK PESANTREN', 'STATUS ASAL SANTRI', 'SEKOLAH ASAL', 'ALAMAT SEKOLAH ASAL',
                        'WILAYAH', 'LEMBAGA', 'DINIYAH', 'TAHUN PELAJARAN', 
                        'NAMA AYAH', 'STATUS HIDUP AYAH', 'PENDIDIKAN AYAH', 'PEKERJAAN AYAH', 'NO HP AYAH',
                        'NAMA IBU', 'STATUS HIDUP IBU', 'PENDIDIKAN IBU', 'PEKERJAAN IBU', 'NO HP IBU',
                        'NAMA WALI', 'PENDIDIKAN WALI', 'PEKERJAAN WALI', 'NO HP WALI', 'PENGHASILAN ORANG TUA ATAU WALI PERBULAN' ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
        
            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            
            
            rows = queryset.filter(wilayah=request.user.wilayah).values_list('nis', 'nisn', 'nik', 'no_kk', 'nama', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'agama', 'alamat', 'kecamatan', 'kabupaten', 'propinsi', 'hobi', 'cita_cita', 'anak_ke', 'jumlah_saudara', 'tanggal_masuk_pesantren', 'status_asal_santri', 'sekolah_asal', 'alamat_sekolah_asal',
                        'wilayah', 'lembaga', 'diniyah', 'tahun_pelajaran',
                        'nama_ayah', 'status_hidup_ayah', 'pendidikan_ayah', 'pekerjaan_ayah', 'no_hp_ayah',
                        'nama_ibu', 'status_hidup_ibu', 'pendidikan_ibu', 'pekerjaan_ibu', 'no_hp_ibu',
                        'nama_wali', 'pendidikan_wali', 'pekerjaan_wali', 'no_hp_wali', 'penghasilan_orang_tua_atau_wali_perbulan' )
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        
            wb.save(response)
            return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
            "menu": "export_santriwilayah",
        }
    return render(request, 'appsantri/export_santriwilayah.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def form_santri(request):
    formsantri = FormSantri()
    if request.method == 'POST':
        formsimpan = FormSantri(request.POST, request.FILES)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('santri')
    context={
        'judul': 'Halaman Form Santri',
        'menu': 'santri',
        'form': formsantri
    }

    return render(request, 'appsantri/form_santri.html', context)

@login_required(login_url='login') 
@ijinkan_pengguna(yang_diizinkan=['admin'])   
def edit_santri(request, pk):
    santri = Santri.objects.get(id=pk)
    formsantri = FormSantri(instance=santri)
    if request.method == 'POST':
        formsimpan = FormSantri(request.POST, request.FILES, instance=santri)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('santri')
    context={
        'judul': 'Halaman Form Santri',
        'menu': 'santri',
        'form': formsantri
    }

    return render(request, 'appsantri/form_santri.html', context)

@login_required(login_url='login') 
@ijinkan_pengguna(yang_diizinkan=['admin'])
def render_pdf_view(request, pk):
    detailsantri = Santri.objects.get(id=pk)

    template_path = 'appsantri/pdf.html'
    context = {'detailsantri': detailsantri}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# pdf lembaga
@login_required(login_url='login') 
@ijinkan_pengguna(yang_diizinkan=['lembaga'])
def render_pdf_lembaga_view(request, pk):
    detailsantri = Santri.objects.get(id=pk)

    template_path = 'appsantri/pdf_lembaga.html'
    context = {'detailsantri': detailsantri}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
# /pdf lembaga

# pdf diniyah
@login_required(login_url='login') 
@ijinkan_pengguna(yang_diizinkan=['diniyah'])
def render_pdf_diniyah_view(request, pk):
    detailsantri = Santri.objects.get(id=pk)

    template_path = 'appsantri/pdf_diniyah.html'
    context = {'detailsantri': detailsantri}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
# /pdf diniyah

# pdf wilayah
@login_required(login_url='login') 
@ijinkan_pengguna(yang_diizinkan=['wilayah'])
def render_pdf_wilayah_view(request, pk):
    detailsantri = Santri.objects.get(id=pk)

    template_path = 'appsantri/pdf_wilayah.html'
    context = {'detailsantri': detailsantri}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
# /pdf wilayah

@login_required(login_url='login') 
def grafik(request):
    labels = []
    data = []

    da = Lembaga.objects.all()
 
    appsantri = Santri.objects.values('lembaga__nama').annotate(total=Count('lembaga')).order_by('-total')
    for r in appsantri:
        labels.append(r['lembaga__nama'])
        data.append(r['total'])

    context={
        'judul': 'Halaman Grafik',
        'menu': 'grafik',
        'labels':labels,
        'data' : data,
        'da' : da,
        
    }
    return render(request, 'appsantri/grafik.html', context)

@login_required(login_url='login') 
def grafik2(request):
    labels = []
    data = []

    appsantri = Santri.objects.values('diniyah__nama').annotate(total=Count('diniyah')).order_by('-total').filter(~Q(diniyah__nama=None))
    for r in appsantri:
        labels.append(r['diniyah__nama'])
        data.append(r['total'])

    context={
        'judul': 'Halaman Grafik',
        'menu': 'grafik2',
        'labels':labels,
        'data' : data,
    }
    return render(request, 'appsantri/grafik2.html', context)

@login_required(login_url='login') 
def grafik3(request):
    labels = []
    data = []

    appsantri = Santri.objects.all().values('wilayah__nama').annotate(total=Count('wilayah')).order_by('-total').filter(~Q(wilayah__nama=None))
    for r in appsantri:
        labels.append(r['wilayah__nama'])
        data.append(r['total'])

    context={
        'judul': 'Halaman Grafik',
        'menu': 'grafik3',
        'labels':labels,
        'data' : data,
    }
    return render(request, 'appsantri/grafik3.html', context)








        
from django.shortcuts import render, redirect, get_object_or_404
from .models import CatatanHutang

# Create your views here.
def home(request):
  data = {
    'title': 'Beranda',
    'hutang': CatatanHutang.objects.all()
  }

  return render(request, 'home.html', data)

def tambah_data(request):
    if request.method == 'POST':
        CatatanHutang.objects.create(
            nama_pemberi=request.POST.get('nama_pemberi'),
            nama_peminjam=request.POST.get('nama_peminjam'),
            jumlah=request.POST.get('jumlah'),
            tanggal_pinjam=request.POST.get('tanggal_pinjam'),
            tanggal_jatuh_tempo=request.POST.get('tanggal_jatuh_tempo') or None,
            catatan=request.POST.get('catatan'),
        )
        return redirect('home')
    
    data = {'title': 'Tambah Data'}
    return render(request, 'tambah_data.html', data)

def edit_data(request, pk):
    hutang = get_object_or_404(CatatanHutang, pk=pk)
    if request.method == 'POST':
        hutang.nama_pemberi = request.POST.get('nama_pemberi')
        hutang.nama_peminjam = request.POST.get('nama_peminjam')
        hutang.jumlah = request.POST.get('jumlah')
        hutang.tanggal_pinjam = request.POST.get('tanggal_pinjam')
        hutang.tanggal_jatuh_tempo = request.POST.get('tanggal_jatuh_tempo') or None
        hutang.status = request.POST.get('status')
        hutang.catatan = request.POST.get('catatan')
        hutang.save()
        return redirect('home')
    
    data = {'title': 'Edit Data', 'hutang': hutang}
    return render(request, 'edit_data.html', data)

def hapus_data(request, pk):
    hutang = get_object_or_404(CatatanHutang, pk=pk)
    if request.method == 'POST':
        hutang.delete()
        return redirect('home')
    
    return redirect('home')
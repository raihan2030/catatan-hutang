from django.db import models

# Create your models here.
class CatatanHutang(models.Model):
    STATUS_CHOICES = [
        ('belum_lunas', 'Belum Lunas'),
        ('lunas', 'Lunas'),
    ]

    nama_pemberi = models.CharField(max_length=100)
    nama_peminjam = models.CharField(max_length=100)
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)
    tanggal_pinjam = models.DateField()
    tanggal_jatuh_tempo = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='belum_lunas')
    catatan = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nama_peminjam} pinjam {self.jumlah} dari {self.nama_pemberi}"
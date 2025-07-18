# Generated by Django 4.2.11 on 2025-06-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatatanHutang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pemberi', models.CharField(max_length=100)),
                ('nama_peminjam', models.CharField(max_length=100)),
                ('jumlah', models.DecimalField(decimal_places=2, max_digits=12)),
                ('tanggal_pinjam', models.DateField()),
                ('tanggal_jatuh_tempo', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('belum_lunas', 'Belum Lunas'), ('lunas', 'Lunas')], default='belum_lunas', max_length=12)),
                ('catatan', models.TextField(blank=True)),
            ],
        ),
    ]

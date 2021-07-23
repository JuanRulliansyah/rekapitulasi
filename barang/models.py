from django.db import models


class Barang(models.Model):
    class StatusPengiriman(models.TextChoices):
        barang_masuk = 'barang_masuk', 'Barang Masuk'
        barang_keluar = 'perjalanan', 'Barang Keluar'

    kode = models.CharField(max_length=100)
    nama = models.CharField(max_length=255)
    kategori_barang = models.ForeignKey(
        'kategori.Kategori',
        related_name='barang',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.nama
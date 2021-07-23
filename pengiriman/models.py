from django.db import models


class Pengiriman(models.Model):
    class StatusPengiriman(models.TextChoices):
        barang_masuk = 'barang_masuk', 'Barang Masuk'
        barang_keluar = 'perjalanan', 'Barang Keluar'

    status = models.CharField(
        'status pengiriman',
        max_length=100,
        choices=StatusPengiriman.choices,
        blank=False,
        null=False
    )
    petugas = models.ForeignKey(
        'petugas.Petugas',
        related_name='pengiriman',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    supir = models.ForeignKey(
        'supir.Supir',
        related_name='pengiriman',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    barang = models.ForeignKey(
        'barang.Barang',
        related_name='pengiriman',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    supplier = models.ForeignKey(
        'supplier.Supplier',
        related_name='pengiriman',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    alamat = models.TextField(default="-")
    qty = models.PositiveSmallIntegerField('quantity', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.barang.nama} {self.status}'

    def admin_action(self, request, queryset):

        actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        pass

    export_as_csv.short_description = "Export Selected"


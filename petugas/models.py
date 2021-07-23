from django.db import models


class Petugas(models.Model):
    nama = models.CharField(max_length=255)
    jabatan = models.ForeignKey(
        'jabatan.Jabatan',
        related_name='petugas',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    nip = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

from django.db import models


class Supir(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    nip = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

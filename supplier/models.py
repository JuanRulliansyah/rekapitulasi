from django.db import models


class Supplier(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

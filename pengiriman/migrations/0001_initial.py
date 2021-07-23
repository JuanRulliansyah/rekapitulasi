# Generated by Django 3.2.5 on 2021-07-14 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        ('supir', '0001_initial'),
        ('barang', '0001_initial'),
        ('petugas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pengiriman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('barang_masuk', 'Barang Masuk'), ('perjalanan', 'Barang Keluar')], max_length=100, verbose_name='status pengiriman')),
                ('qty', models.PositiveSmallIntegerField(default=0, verbose_name='quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('barang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pengiriman', to='barang.barang')),
                ('petugas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pengiriman', to='petugas.petugas')),
                ('supir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pengiriman', to='supir.supir')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pengiriman', to='supplier.supplier')),
            ],
        ),
    ]

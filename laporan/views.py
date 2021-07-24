import csv

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from pengiriman.models import Pengiriman


def laporan_view(request):
    return render(request, 'laporan/index.html/')

def ekspor_view(request):

    request = request
    if request.method == "POST":
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow(['Status', 'Petugas', 'Supir', 'Barang', 'Supplier', 'Alamat', 'Qty', 'Pada'])

        for pengiriman in Pengiriman.objects.filter(
                Q(created_at__range=[request.POST.get('date_start'), request.POST.get('date_end')]),
                Q(status=request.POST.get('status'))
        ):
            data_pengiriman = [pengiriman.status, pengiriman.petugas.nama, pengiriman.supir.nama,
                               pengiriman.barang.nama, pengiriman.supplier.nama, pengiriman.alamat, pengiriman.qty,
                               pengiriman.created_at]

            writer.writerow(data_pengiriman)

        response['Content-Disposition'] = 'attachment; filename="pengiriman.csv"'

        return response
from django.shortcuts import render

def laporan_view(request):
    return render(request, 'laporan/index.html/')

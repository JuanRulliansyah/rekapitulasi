from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.template.response import TemplateResponse
from django.urls import path

from pengiriman.models import Pengiriman

class PengirimanAdmin(admin.ModelAdmin):

    @staff_member_required
    def export(self, request):
        pengiriman = Pengiriman.objects.all()
        context = dict(
            self.admin_site.each_context(request),
        )
        opts = self.opts
        app_label = opts.app_label
        context.update({
            'opts': opts,
            'app_label': app_label,
            'pengiriman': pengiriman
        })
        return TemplateResponse(request, "../pengiriman/templates/admin/change_list.html", context)

    def get_urls(self):
        urls = super(PengirimanAdmin, self).get_urls()
        urlpatterns = [
            path('ekspor/', self.export),
        ]
        return urlpatterns + urls

admin.site.register(Pengiriman, PengirimanAdmin)

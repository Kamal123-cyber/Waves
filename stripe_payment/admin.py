from django.contrib import admin
from .models import StripePayment
from django.contrib import messages
from io import BytesIO
from django.template.loader import render_to_string
import os
import pdfkit
import tempfile
import zipfile
from django.http import HttpResponse
# Register your models here.
class StripePaymentAdmin(admin.ModelAdmin):
    list_display = ['name','email','billing_address','stripe_session_id','status']
    actions = ['download_invoices']


    def download_invoices(modeladmin, request, queryset):
        options = {
            'page-size': 'Letter',
            'encoding': 'UTF-8',
            'no-outline': None
        }
        config = pdfkit.configuration(wkhtmltopdf='bin/wkhtmltopdf')
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, mode='w') as zip_file:
            for stripe_payment in queryset:
                if not stripe_payment:
                    messages.warning(request, f'Invoice for transaction {stripe_payment.id} is not available.')
                    continue
                with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_file:
                    invoice_html = render_to_string('invoice.html', {'payment': stripe_payment})
                    temp_file.write(invoice_html.encode('utf-8'))
                pdf_bytes = pdfkit.from_file(temp_file.name, False, options=options, configuration=config)
                pdf_filename = f'{stripe_payment.name}.pdf'
                zip_file.writestr(pdf_filename, pdf_bytes)
                os.unlink(temp_file.name)
        zip_buffer.seek(0)
        response = HttpResponse(zip_buffer, content_type='application/x-zip-compressed')
        response['Content-Disposition'] = 'attachment; filename="invoices.zip"'
        return response

    download_invoices.short_description = 'Download selected invoice'

admin.site.register(StripePayment, StripePaymentAdmin)

import pytest
from rest_framework import status
from django.urls import reverse
from invoices.models import Invoice, InvoiceDetail

@pytest.mark.django_db
class TestInvoiceAPI:
    def setup_method(self, method):
        self.invoice = Invoice.objects.create(date='2024-02-20', customer_name='Test Customer')
        self.detail = InvoiceDetail.objects.create(invoice=self.invoice, description='Test Item', quantity=2, unit_price=10)

    def test_invoice_list(self, client):
        url = reverse('invoice-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_invoice_detail(self, client):
        url = reverse('invoice-detail-detail', kwargs={'invoice_id': self.invoice.id, 'detail_id': self.detail.id})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == 'Test Item'

    @pytest.mark.skip
    def test_create_invoice_detail(self, client):
        url = reverse('invoice-detail-list', kwargs={'invoice_id': self.invoice.id})
        data = {'description': 'New Item', 'quantity': 3, 'unit_price': 15}
        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert InvoiceDetail.objects.filter(description='New Item').count() == 1

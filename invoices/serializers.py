from rest_framework import serializers
from .models import Invoice, InvoiceDetail


class InvoiceDetailSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = InvoiceDetail
        fields = ['id', 'invoice', 'description', 'quantity', 'unit_price', 'price']

    def get_price(self, obj):
        return obj.quantity * obj.unit_price


class InvoiceSerializer(serializers.ModelSerializer):
    details_url = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ['id', 'date', 'customer_name', 'details_url']

    def get_details_url(self, obj):
        return f'http://127.0.0.1:8000/api/invoices/{obj.id}/details/'

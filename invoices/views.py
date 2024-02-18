from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from rest_framework import viewsets, generics


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetailListCreateView(generics.ListCreateAPIView):
    serializer_class = InvoiceDetailSerializer

    def get_queryset(self):
        invoice_id = self.kwargs['invoice_id']
        return InvoiceDetail.objects.filter(invoice_id=invoice_id)

    def perform_create(self, serializer):
        invoice_id = self.kwargs['invoice_id']
        serializer.save(invoice_id=invoice_id)


class InvoiceDetailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer

    def get_object(self):
        invoice_id = self.kwargs['invoice_id']
        detail_id = self.kwargs['detail_id']
        return InvoiceDetail.objects.get(id=detail_id, invoice_id=invoice_id)

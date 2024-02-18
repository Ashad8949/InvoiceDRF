from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailListCreateView, InvoiceDetailRetrieveUpdateDestroyView

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('invoices/<int:invoice_id>/details/', InvoiceDetailListCreateView.as_view(), name='invoice-detail-list'),
    path('invoices/<int:invoice_id>/details/<int:detail_id>/', InvoiceDetailRetrieveUpdateDestroyView.as_view(),name='invoice-detail-detail'),
]

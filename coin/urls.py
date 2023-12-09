from django.urls import path
from .views import HealthCheckView, AddressDetailsView, AddressTransactionsView, TransactionDetailsView

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('address/<str:address>/', AddressDetailsView.as_view(), name='address-details'),
    path('address/transactions/<str:address>/', AddressTransactionsView.as_view(), name='address-transactions'),
    path('transaction/<str:tx_hash>/', TransactionDetailsView.as_view(), name='transaction-details'),
]

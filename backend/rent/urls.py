from django.urls import path
from rent.views import RentAPIView, ProductAPIView, RentProductAPIView

urlpatterns = [
    path('rent/', RentAPIView.as_view(), name='rent'),
    path('product/', ProductAPIView.as_view(), name='product'),
    path('rent-product/', RentProductAPIView.as_view(), name='rent_product'),
]

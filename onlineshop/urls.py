from django.urls import path
from onlineshop.views import OrderView , ProductView ,ProductRetriveUpdateDestroyView



urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
    path('products/',ProductView.as_view(),name='products'),
    path('products/<int:pk>', ProductRetriveUpdateDestroyView.as_view(), name="product-detail")
]

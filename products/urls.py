from django.urls import path
from products.views import ProductListView, ProductTemplateView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='shop'),
    path('detail/', ProductTemplateView.as_view(), name='product-detail'),
]
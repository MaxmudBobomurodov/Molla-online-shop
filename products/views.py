from django.views.generic import TemplateView, ListView

from products.models import ProductModel, ProductCategory, ProductSize, ProductColor, ProductBrand


class ProductListView(ListView):
    model = ProductModel
    template_name = 'shop/shop.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['sizes'] = ProductSize.objects.all()
        context['colors'] = ProductColor.objects.all()
        context['brands'] = ProductBrand.objects.all()
        return context


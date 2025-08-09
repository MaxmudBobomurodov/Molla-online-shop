from django.views.generic import TemplateView, ListView, DetailView

from products.models import ProductModel, ProductCategory, ProductSize, ProductColor, ProductBrand


class ProductListView(ListView):
    model = ProductModel
    template_name = 'shop/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        size = self.request.GET.get('size')
        color = self.request.GET.get('color')
        brand = self.request.GET.get('brand')
        price = self.request.GET.get('price')

        if q:
            qs = qs.filter(title__icontains=q)
        if cat:
            qs = qs.filter(categories=cat)
        if size:
            qs = qs.filter(products_quantity__sizes=size)
        if color:
            qs = qs.filter(products_quantity__colors=color)
        if brand:
            qs = qs.filter(brand=brand)
        # if price:
        #     qs = qs.filter(categories__products__price=q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['sizes'] = ProductSize.objects.all()
        context['colors'] = ProductColor.objects.all()
        context['brands'] = ProductBrand.objects.all()
        return context


class ProductTemplateView(TemplateView):
    model = ProductModel
    template_name = "shop/product.html"
    context_object_name = 'product'
